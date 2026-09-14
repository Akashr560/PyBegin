# === Student CGPA Calculator · annotated for the pyBegin playground ===

GRADE_POINTS = {
    "A+": 10, "A": 9, "B+": 8, "B": 7,
    "C+": 6, "C": 5, "D": 4, "F": 0
}

student_name = input("Enter Student Name: ")
reg_number = input("Enter Register Number: ")
num_subjects = int(input("Enter Number of Subjects: "))

subjects = []
for i in range(1, num_subjects + 1):
    sub_name = input(f"Subject {i} Name: ")
    grade = input(f"Grade for {sub_name} (A+, A, B+, B, C+, C, D, F): ").strip().upper()
    credit = float(input(f"Credits for {sub_name}: "))
    point = GRADE_POINTS.get(grade, 0)
    subjects.append({"name": sub_name, "grade": grade, "point": point, "credit": credit})

total_credits = sum(s["credit"] for s in subjects)
weighted_points = sum(s["point"] * s["credit"] for s in subjects)
cgpa = weighted_points / total_credits if total_credits > 0 else 0.0

if cgpa >= 9.0:
    performance = "EXCELLENT"
elif cgpa >= 8.0:
    performance = "VERY GOOD"
elif cgpa >= 7.0:
    performance = "GOOD"
elif cgpa >= 6.0:
    performance = "AVERAGE"
elif cgpa >= 5.0:
    performance = "NEEDS IMPROVEMENT"
else:
    performance = "POOR"

print()
print("========================================")
print("          STUDENT CGPA CALCULATOR       ")
print("========================================\n")
print(f"Student Name    : {student_name}")
print(f"Register Number : {reg_number}\n")
print("Subject Details")
print("----------------------------------------")
print(f"{'Subject':<12} {'Grade':<8} {'Grade Point':<12} {'Credit':<6}")
for s in subjects:
    print(f"{s['name']:<12} {s['grade']:<8} {s['point']:<12} {s['credit']:<6}")
print("----------------------------------------")
print(f"Total Credits  : {total_credits}")
print(f"CGPA           : {cgpa:.2f}")
print(f"Performance    : {performance}")
print("========================================")
