# Student CGPA Calculator

A beginner-friendly command-line Python application that calculates a student's Cumulative Grade Point Average (CGPA) based on letter grades and credits across multiple subjects.

This is a beginner-friendly Python educational project contributed to the open-source [Python Beginner Projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects) repository.

---

## 📌 Features

- **Dynamic Subject Entry**: Prompts for student details, subject names, letter grades, and credit hours.
- **Weighted CGPA Calculation**: Computes credit-weighted CGPA accurately using the grade-point scale.
- **Academic Performance Classification**: Categorizes performance from `EXCELLENT` to `POOR`.
- **Robust Input Validation**:
  - Validates non-empty Student Name, Register Number, and Subject Names.
  - Ensures Number of Subjects is greater than `0`.
  - Enforces valid letter grades (`A+`, `A`, `B+`, `B`, `C+`, `C`, `D`, `F`).
  - Ensures credits are numeric and greater than `0`.
  - Prevents division-by-zero errors.
- **Clean Console Output**: Displays a formatted academic summary table.

---

## 📊 Grade-Point System

| Letter Grade | Grade Point |
| :---: | :---: |
| **A+** | **10** |
| **A** | **9** |
| **B+** | **8** |
| **B** | **7** |
| **C+** | **6** |
| **C** | **5** |
| **D** | **4** |
| **F** | **0** |

---

## 📐 CGPA Formula

$$\text{CGPA} = \frac{\sum (\text{Grade Point} \times \text{Credit})}{\sum \text{Credit}}$$

---

## 🏆 Performance Classification

| CGPA Range | Performance Classification |
| :---: | :---: |
| **9.0 – 10.0** | **EXCELLENT** |
| **8.0 – 8.99** | **VERY GOOD** |
| **7.0 – 7.99** | **GOOD** |
| **6.0 – 6.99** | **AVERAGE** |
| **5.0 – 5.99** | **NEEDS IMPROVEMENT** |
| **Below 5.0** | **POOR** |

---

## 🛠️ Requirements

- Python 3.x (Uses Python standard library only — no external packages required).

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd projects/Student-CGPA-Calculator
   ```
3. Run the Python script:
   ```bash
   python cgpa_calculator.py
   ```

---

## 💻 Example Usage

### Example Input
```text
Enter Student Name: Akash
Enter Register Number: 23CS001
Enter Number of Subjects: 4

Subject 1 Name: Java
Grade for Java: A
Credits for Java: 4

Subject 2 Name: Python
Grade for Python: A+
Credits for Python: 3

Subject 3 Name: Database
Grade for Database: B+
Credits for Database: 4

Subject 4 Name: Web
Grade for Web: A
Credits for Web: 3
```

### Example Output
```text
========================================
          STUDENT CGPA CALCULATOR
========================================

Student Name    : Akash
Register Number : 23CS001

Subject Details
----------------------------------------
Subject      Grade    Grade Point    Credit
Java           A          9             4
Python        A+         10             3
Database      B+          8             4
Web            A          9             3
----------------------------------------
Total Credits  : 14
CGPA           : 9.00
Performance    : EXCELLENT
========================================
```

---

## 🔮 Future Improvements

- Support semester-wise CGPA calculation and tracking.
- Add export options to save CGPA transcripts to text or CSV files.
- Add a Graphical User Interface (GUI) using `tkinter`.
