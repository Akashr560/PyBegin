"""
Student Grade Calculator

A beginner-friendly Python command-line application to calculate total marks,
average, percentage, letter grade, pass/fail status, highest and lowest marks
for a student across multiple subjects.
"""


def get_non_empty_string(prompt: str) -> str:
    """Prompt the user for a non-empty string input."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Error: Input cannot be empty. Please try again.\n")


def get_positive_integer(prompt: str) -> int:
    """Prompt the user for an integer greater than 0 with validation."""
    while True:
        user_input = input(prompt).strip()
        try:
            val = int(user_input)
            if val > 0:
                return val
            print("Error: Number of subjects must be greater than 0.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number.\n")


def get_valid_mark(prompt: str) -> float:
    """Prompt the user for a mark between 0 and 100 inclusive."""
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            if 0 <= val <= 100:
                # Return integer if it's a whole number for cleaner display
                return int(val) if val.is_integer() else val
            print("Error: Marks must be between 0 and 100.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid numeric mark.\n")


def calculate_grade(percentage: float) -> str:
    """
    Determine letter grade based on percentage:
    90–100 -> A+
    80–89  -> A
    70–79  -> B
    60–69  -> C
    50–59  -> D
    40–49  -> E
    Below 40 -> F
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_subject_marks(num_subjects: int):
    """Collect subject names and marks for the given number of subjects."""
    subject_marks = []
    print(f"\nEnter details for {num_subjects} subjects (out of 100):\n")
    for i in range(1, num_subjects + 1):
        subject_name = get_non_empty_string(f"Subject {i} Name: ")
        mark = get_valid_mark(f"Marks for {subject_name}: ")
        subject_marks.append((subject_name, mark))
        print()
    return subject_marks


def calculate_results(subject_marks):
    """
    Calculate summary statistics:
    total, average, percentage, grade, pass/fail status, highest and lowest marks.
    """
    marks = [mark for _, mark in subject_marks]
    total_marks = sum(marks)
    num_subjects = len(marks)
    average = total_marks / num_subjects
    percentage = average
    grade = calculate_grade(percentage)

    # PASS if every subject is >= 40, else FAIL
    status = "PASS" if all(m >= 40 for m in marks) else "FAIL"

    highest_mark = max(marks)
    lowest_mark = min(marks)

    return {
        "total": total_marks,
        "average": average,
        "percentage": percentage,
        "grade": grade,
        "status": status,
        "highest": highest_mark,
        "lowest": lowest_mark,
    }


def display_result(student_name: str, reg_number: str, subject_marks, results):
    """Display a clean formatted summary report to the console."""
    print("\n========================================")
    print("        STUDENT GRADE CALCULATOR        ")
    print("========================================\n")
    print(f"Student Name    : {student_name}")
    print(f"Register Number : {reg_number}\n")
    print("Subject Marks")
    print("----------------------------------------")
    for subject, mark in subject_marks:
        print(f"{subject:<16} : {mark}")
    print("----------------------------------------")
    print(f"Total Marks     : {results['total']}")
    print(f"Average         : {results['average']:.2f}")
    print(f"Percentage      : {results['percentage']:.2f}%")
    print(f"Grade           : {results['grade']}")
    print(f"Status          : {results['status']}")
    print(f"Highest Mark    : {results['highest']}")
    print(f"Lowest Mark     : {results['lowest']}")
    print("========================================\n")


def main():
    """Main execution function for Student Grade Calculator."""
    print("========================================")
    print("        STUDENT GRADE CALCULATOR        ")
    print("========================================\n")

    student_name = get_non_empty_string("Enter Student Name: ")
    reg_number = get_non_empty_string("Enter Register Number: ")
    num_subjects = get_positive_integer("Enter Number of Subjects: ")

    subject_marks = get_subject_marks(num_subjects)
    results = calculate_results(subject_marks)

    display_result(student_name, reg_number, subject_marks, results)


if __name__ == "__main__":
    main()
