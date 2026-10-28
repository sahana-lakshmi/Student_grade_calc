def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    return {
        "total": total,
        "average": average
    }

if __name__ == "__main__":
    print("Student Grade Calculator V)")
    try:
        user_input = input("Enter marks separated by spaces: ")
        student_marks = [float(x) for x in user_input.split()]
        if not student_marks:
            print("No marks entered.")
        else:
            res = calculate_results(student_marks)
            print(f"Total Marks: {res['total']}")
            print(f"Average Marks: {res['average']:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
