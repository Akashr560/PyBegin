# === Student Attendance Analyzer · annotated for the pyBegin playground ===

# Get student details and attendance inputs
student_name = input("Enter Student Name: ")
register_number = input("Enter Register Number: ")
total_working_days = int(input("Enter Total Working Days: "))
present_days = int(input("Enter Present Days: "))

# Calculate absent days and attendance percentage
absent_days = total_working_days - present_days
percentage = (present_days / total_working_days) * 100.0

# Determine eligibility (75% threshold)
if percentage >= 75.0:
    status = "ELIGIBLE"
else:
    status = "NOT ELIGIBLE"

# Display formatted report
print()
print("========================================")
print("STUDENT ATTENDANCE ANALYZER")
print("===========================")
print(f"Student Name    : {student_name}")
print(f"Register Number : {register_number}")
print(f"Working Days    : {total_working_days}")
print(f"Present Days    : {present_days}")
print(f"Absent Days     : {absent_days}")
print(f"Attendance      : {percentage:.2f}%")
print(f"Status          : {status}")
print("========================================")
