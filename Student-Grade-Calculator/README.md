# Student Grade Calculator

A beginner-friendly command-line Python application that calculates total marks, average, percentage, letter grade, pass/fail status, highest mark, and lowest mark for a student across multiple subjects.

This is a beginner-friendly Python educational project contributed to the open-source [Python Beginner Projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects) repository.

---

## 📌 Features

- **Dynamic Subject Entry**: Prompts for student details and allows inputting marks for any number of subjects.
- **Comprehensive Calculations**: Computes total marks, average, percentage, grade, pass/fail status, highest mark, and lowest mark.
- **Robust Input Validation**:
  - Ensures Student Name, Register Number, and Subject Names are non-empty.
  - Ensures Number of Subjects is greater than `0`.
  - Ensures marks are numeric and between `0` and `100`.
  - Prevents program crashes from invalid user inputs.
- **Clean Console Output**: Displays a formatted academic report.

---

## 📊 Grade Calculation System

The letter grade is assigned based on the overall percentage (out of 100):

| Percentage Range | Grade |
| :---: | :---: |
| **90 – 100%** | **A+** |
| **80 – 89%** | **A** |
| **70 – 79%** | **B** |
| **60 – 69%** | **C** |
| **50 – 59%** | **D** |
| **40 – 49%** | **E** |
| **Below 40%** | **F** |

---

## 🎯 Pass / Fail Rules

- **PASS**: Every subject mark must be **40 or above** ($\ge 40$).
- **FAIL**: If **any** subject mark is **below 40** ($< 40$), the overall status is marked as `FAIL`.

---

## 🛠️ Requirements

- Python 3.x (Uses Python standard library only — no external packages required).

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd projects/Student-Grade-Calculator
   ```
3. Run the Python script:
   ```bash
   python grade_calculator.py
   ```

---

## 💻 Example Usage

### Example Input
```text
Enter Student Name: Akash
Enter Register Number: 23CS001
Enter Number of Subjects: 5

Subject 1 Name: Java
Marks for Java: 85

Subject 2 Name: Python
Marks for Python: 90

Subject 3 Name: Database
Marks for Database: 78

Subject 4 Name: Web Development
Marks for Web Development: 88

Subject 5 Name: Data Science
Marks for Data Science: 92
```

### Example Output
```text
========================================
        STUDENT GRADE CALCULATOR
========================================

Student Name    : Akash
Register Number : 23CS001

Subject Marks
----------------------------------------
Java            : 85
Python          : 90
Database        : 78
Web Development : 88
Data Science    : 92
----------------------------------------
Total Marks     : 433
Average         : 86.60
Percentage      : 86.60%
Grade           : A
Status          : PASS
Highest Mark    : 92
Lowest Mark     : 78
========================================
```

---

## 🔮 Future Improvements

- Add export feature to save grade reports as PDF or text files.
- Add a Graphical User Interface (GUI) using `tkinter`.
- Allow customizable pass thresholds and grade scale rules.
