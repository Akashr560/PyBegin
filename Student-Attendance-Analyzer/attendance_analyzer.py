"""
Student Attendance Analyzer

A beginner-friendly Python command-line application to analyze student attendance,
calculate attendance percentages, absent days, and determine exam eligibility.
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
            print("Error: Total working days must be greater than 0.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number.\n")


def get_valid_present_days(prompt: str, total_working_days: int) -> int:
    """
    Prompt the user for present days ensuring 0 <= present_days <= total_working_days.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            val = int(user_input)
            if val < 0:
                print("Error: Present days cannot be negative.\n")
            elif val > total_working_days:
                print(
                    f"Error: Present days ({val}) cannot be greater than total working days ({total_working_days}).\n"
                )
            else:
                return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number.\n")


def calculate_attendance(total_working_days: int, present_days: int):
    """
    Calculate absent days, attendance percentage, and eligibility status.

    Formula:
    Attendance Percentage = (Present Days / Total Working Days) * 100

    Threshold:
    75% or above -> ELIGIBLE
    Below 75%    -> NOT ELIGIBLE
    """
    absent_days = total_working_days - present_days
    percentage = (present_days / total_working_days) * 100.0
    status = "ELIGIBLE" if percentage >= 75.0 else "NOT ELIGIBLE"
    return absent_days, percentage, status


def display_report(
    student_name: str,
    register_number: str,
    total_working_days: int,
    present_days: int,
    absent_days: int,
    percentage: float,
    status: str,
):
    """Display a formatted attendance summary report to the console."""
    print("\n========================================")
    print("STUDENT ATTENDANCE ANALYZER")
    print("===========================")
    print(f"Student Name    : {student_name}")
    print(f"Register Number : {register_number}")
    print(f"Working Days    : {total_working_days}")
    print(f"Present Days    : {present_days}")
    print(f"Absent Days     : {absent_days}")
    print(f"Attendance      : {percentage:.2f}%")
    print(f"Status          : {status}")
    print("========================================\n")


def main():
    """Main execution function for Student Attendance Analyzer."""
    print("========================================")
    print("      STUDENT ATTENDANCE ANALYZER       ")
    print("========================================\n")

    student_name = get_non_empty_string("Enter Student Name: ")
    register_number = get_non_empty_string("Enter Register Number: ")
    total_working_days = get_positive_integer("Enter Total Working Days: ")
    present_days = get_valid_present_days(
        "Enter Present Days: ", total_working_days
    )

    absent_days, percentage, status = calculate_attendance(
        total_working_days, present_days
    )

    display_report(
        student_name,
        register_number,
        total_working_days,
        present_days,
        absent_days,
        percentage,
        status,
    )


if __name__ == "__main__":
    main()
