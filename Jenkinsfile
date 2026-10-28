pipeline {
    agent any

    environment {
        // Defines the unique image tag using the Git commit hash (First 7 characters)
        IMAGE_TAG        = "${GIT_COMMIT.take(7)}"
        // Jenkins Credentials ID containing your Docker Hub username/password
        DOCKER_CREDS_ID  = 'dockerhub-credentials'
        // Jenkins Credentials ID containing your Kubeconfig file
        KUBE_CREDS_ID    = 'kubeconfig-credentials'
        // Replace with your actual Docker Hub Profile Username
        DOCKER_USER      = 'your_dockerhub_username'
        IMAGE_NAME       = 'student-calc'
    }

    stages {
        // Stage 1 & 2 (Source Code & Version Control) are handled natively by Jenkins checkout
        stage('Stage 3: Continuous Integration (Test)') {
            steps {
                echo 'Setting up Python environment and running automated tests...'
                // Assumes your Jenkins node has Python 3 and pip installed
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Stage 4: Build & Push Container') {
            steps {
                echo "Building Docker image version: ${IMAGE_TAG}"
                script {
                    // Logs into Docker Hub, builds the container image, and pushes it
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDS_ID, 
                                                     usernameVariable: 'DOCKER_USER_ENV', 
                                                     passwordVariable: 'DOCKER_PASS_ENV')]) {
                        
                        sh "docker login -u ${DOCKER_USER_ENV} -p ${DOCKER_PASS_ENV}"
                        
                        // Build container using local Dockerfile
                        def customImage = docker.build("${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}")
                        
                        // Push the unique image tag to Docker Hub
                        customImage.push()
                    }
                }
            }
        }

        stage('Stage 5: Deployment to Kubernetes') {
            steps {
                echo "Deploying image tag ${IMAGE_TAG} to Kubernetes Cluster..."
                // Utilizes the Kubeconfig file securely stored in Jenkins Credentials
                withKubeConfig([credentialsId: env.KUBE_CREDS_ID]) {
                    sh """
                        # Dynamically substitute the placeholder image tag inside deployment.yaml
                        sed -i "s|DOCKERHUB_USERNAME/student-calc:IMAGE_TAG|${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}|g" k8s/deployment.yaml
                        
                        # Apply configurations to your connected cluster
                        kubectl apply -f k8s/deployment.yaml
                        
                        # Verify deployment status
                        kubectl rollout status deployment/student-calc-deployment
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace artifacts...'
            // Clean local Docker runtime footprints from the Jenkins agent node
            sh "docker rsync || true"
            cleanWs()
        }
        success {
            echo 'Pipeline execution completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check build logs for debugging instructions.'
        }
    }
}
