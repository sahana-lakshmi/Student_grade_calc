def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    
    # Push 2 Requirement: Add grade calculation based on the average
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'
        
    return {
        "total": total,
        "average": average,
        "grade": grade
    }

if __name__ == "__main__":
    print("--- Student Grade Calculator (V2) ---")
    try:
        user_input = input("Enter marks separated by spaces: ")
        student_marks = [float(x) for x in user_input.split()]
        if not student_marks:
            print("No marks entered.")
        else:
            res = calculate_results(student_marks)
            print(f"Total Marks: {res['total']}")
            print(f"Average Marks: {res['average']:.2f}")
            print(f"Assigned Grade: {res['grade']}") # Display grade mapping
    except ValueError:
        print("Invalid input. Please enter numbers only.")
