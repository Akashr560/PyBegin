# === Student Grade Calculator · annotated for the pyBegin playground ===

student_name = input("Enter Student Name: ")
reg_number = input("Enter Register Number: ")
num_subjects = int(input("Enter Number of Subjects: "))

marks = []
subject_marks = []

for i in range(1, num_subjects + 1):
    sub_name = input(f"Subject {i} Name: ")
    m = float(input(f"Marks for {sub_name}: "))
    m_val = int(m) if m.is_integer() else m
    marks.append(m_val)
    subject_marks.append((sub_name, m_val))

total = sum(marks)
avg = total / num_subjects
pct = avg

# Assign Grade
if pct >= 90:
    grade = "A+"
elif pct >= 80:
    grade = "A"
elif pct >= 70:
    grade = "B"
elif pct >= 60:
    grade = "C"
elif pct >= 50:
    grade = "D"
elif pct >= 40:
    grade = "E"
else:
    grade = "F"

status = "PASS" if all(m >= 40 for m in marks) else "FAIL"

print()
print("========================================")
print("        STUDENT GRADE CALCULATOR        ")
print("========================================\n")
print(f"Student Name    : {student_name}")
print(f"Register Number : {reg_number}\n")
print("Subject Marks")
print("----------------------------------------")
for sub, m in subject_marks:
    print(f"{sub:<16} : {m}")
print("----------------------------------------")
print(f"Total Marks     : {total}")
print(f"Average         : {avg:.2f}")
print(f"Percentage      : {pct:.2f}%")
print(f"Grade           : {grade}")
print(f"Status          : {status}")
print(f"Highest Mark    : {max(marks)}")
print(f"Lowest Mark     : {min(marks)}")
print("========================================")
