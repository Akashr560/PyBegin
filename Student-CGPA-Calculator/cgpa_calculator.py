"""
Student CGPA Calculator

A beginner-friendly Python command-line application to calculate a student's
Cumulative Grade Point Average (CGPA) based on letter grades and credits across
multiple subjects.
"""

GRADE_POINTS = {
    "A+": 10,
    "A": 9,
    "B+": 8,
    "B": 7,
    "C+": 6,
    "C": 5,
    "D": 4,
    "F": 0,
}


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


def get_valid_grade(prompt: str) -> str:
    """Prompt the user for a valid letter grade from GRADE_POINTS."""
    valid_grades_str = ", ".join(GRADE_POINTS.keys())
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in GRADE_POINTS:
            return user_input
        print(
            f"Error: Invalid grade '{user_input}'. Allowed grades: {valid_grades_str}\n"
        )


def get_positive_credit(prompt: str):
    """Prompt the user for a numeric credit value greater than 0."""
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            if val > 0:
                return int(val) if val.is_integer() else val
            print("Error: Credits must be greater than 0.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid numeric credit value.\n")


def convert_grade_to_point(grade: str) -> int:
    """Convert a letter grade to its corresponding numerical grade point."""
    return GRADE_POINTS.get(grade.upper(), 0)


def get_performance(cgpa: float) -> str:
    """
    Classify academic performance based on CGPA:
    9.0 - 10.0 -> EXCELLENT
    8.0 - 8.99 -> VERY GOOD
    7.0 - 7.99 -> GOOD
    6.0 - 6.99 -> AVERAGE
    5.0 - 5.99 -> NEEDS IMPROVEMENT
    Below 5.0  -> POOR
    """
    if cgpa >= 9.0:
        return "EXCELLENT"
    elif cgpa >= 8.0:
        return "VERY GOOD"
    elif cgpa >= 7.0:
        return "GOOD"
    elif cgpa >= 6.0:
        return "AVERAGE"
    elif cgpa >= 5.0:
        return "NEEDS IMPROVEMENT"
    else:
        return "POOR"


def get_subject_details(num_subjects: int):
    """Collect subject names, letter grades, grade points, and credits."""
    subjects = []
    print(f"\nEnter details for {num_subjects} subjects:\n")
    for i in range(1, num_subjects + 1):
        subject_name = get_non_empty_string(f"Subject {i} Name: ")
        grade = get_valid_grade(
            f"Grade for {subject_name} (e.g. A+, A, B+, B, C+, C, D, F): "
        )
        credit = get_positive_credit(f"Credits for {subject_name}: ")
        grade_point = convert_grade_to_point(grade)
        subjects.append(
            {
                "name": subject_name,
                "grade": grade,
                "point": grade_point,
                "credit": credit,
            }
        )
        print()
    return subjects


def calculate_cgpa(subjects):
    """
    Calculate total credits, weighted grade points sum, CGPA, and performance.
    Formula: CGPA = Sum(Grade Point * Credit) / Sum(Credit)
    """
    total_credits = sum(s["credit"] for s in subjects)
    if total_credits <= 0:
        return 0.0, 0.0, "POOR"

    weighted_points = sum(s["point"] * s["credit"] for s in subjects)
    cgpa = weighted_points / total_credits
    performance = get_performance(cgpa)

    return total_credits, cgpa, performance


def display_result(
    student_name: str,
    reg_number: str,
    subjects,
    total_credits,
    cgpa,
    performance,
):
    """Display a clean formatted summary report to the console."""
    print("\n========================================")
    print("          STUDENT CGPA CALCULATOR       ")
    print("========================================\n")
    print(f"Student Name    : {student_name}")
    print(f"Register Number : {reg_number}\n")
    print("Subject Details")
    print("----------------------------------------")
    print(f"{'Subject':<12} {'Grade':<8} {'Grade Point':<12} {'Credit':<6}")
    for s in subjects:
        print(
            f"{s['name']:<12} {s['grade']:<8} {s['point']:<12} {s['credit']:<6}"
        )
    print("----------------------------------------")
    print(f"Total Credits  : {total_credits}")
    print(f"CGPA           : {cgpa:.2f}")
    print(f"Performance    : {performance}")
    print("========================================\n")


def main():
    """Main execution function for Student CGPA Calculator."""
    print("========================================")
    print("          STUDENT CGPA CALCULATOR       ")
    print("========================================\n")

    student_name = get_non_empty_string("Enter Student Name: ")
    reg_number = get_non_empty_string("Enter Register Number: ")
    num_subjects = get_positive_integer("Enter Number of Subjects: ")

    subjects = get_subject_details(num_subjects)
    total_credits, cgpa, performance = calculate_cgpa(subjects)

    display_result(
        student_name, reg_number, subjects, total_credits, cgpa, performance
    )


if __name__ == "__main__":
    main()
