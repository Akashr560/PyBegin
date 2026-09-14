# Student Attendance Analyzer

A beginner-friendly Python application that calculates a student's attendance percentage, absent days, and exam eligibility status based on total working days and present days.

It comes with both a **Command-Line Interface (CLI)** and a modern **Graphical User Interface (GUI)** built using Python's standard `tkinter` library.

This is a beginner-friendly Python mini project contributed to the open-source [Python Beginner Projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects) repository.

---

## 📌 Features

### 💻 Command-Line Version (`attendance_analyzer.py`)
- **Interactive CLI**: Prompts for Student Name, Register Number, Total Working Days, and Present Days.
- **Automatic Calculations**: Computes total absent days, attendance percentage, and eligibility status.
- **Robust Input Validation**: Validates non-empty fields, positive numbers, and logical constraints.
- **Console Summary Report**: Displays a clean text report.

### 🎨 Graphical User Interface Version (`attendance_analyzer_gui.py`)
- **Modern Tkinter UI**: Clean student-friendly design with custom color system (`#4F46E5` Indigo Theme).
- **Form Input Card**: Fields for Student Name, Register Number, Total Working Days, and Present Days.
- **Action Buttons**:
  - `Calculate Attendance`: Prominent primary action button.
  - `Reset`: Clears inputs and resets the report view.
- **Interactive Result Section**: Real-time summary display with color-coded status badges:
  - 🟢 **ELIGIBLE** (Green pill for $\ge 75\%$)
  - 🔴 **NOT ELIGIBLE** (Red pill for $< 75\%$)
- **User-Friendly Popups**: Standard error dialogs for invalid numeric or out-of-range inputs.

---

## 📐 Attendance Calculation Formula

$$\text{Attendance Percentage} = \left(\frac{\text{Present Days}}{\text{Total Working Days}}\right) \times 100$$

$$\text{Absent Days} = \text{Total Working Days} - \text{Present Days}$$

---

## 🎯 Eligibility Rule

- **Threshold**: **75.0%**
- **Eligible Status**:
  - Attendance $\ge 75.0\%$ $\rightarrow$ `ELIGIBLE`
  - Attendance $< 75.0\%$ $\rightarrow$ `NOT ELIGIBLE`

---

## 🛠️ Requirements

- Python 3.x (Uses standard library only — `tkinter` included by default).

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd projects/Student-Attendance-Analyzer
   ```

3. **To run the GUI version**:
   ```bash
   python attendance_analyzer_gui.py
   ```

4. **To run the CLI version**:
   ```bash
   python attendance_analyzer.py
   ```

---

## 💻 Example Usage

### CLI Example Output
```text
========================================
STUDENT ATTENDANCE ANALYZER
===========================
Student Name    : Akash
Register Number : 23CS001
Working Days    : 100
Present Days    : 85
Absent Days     : 15
Attendance      : 85.00%
Status          : ELIGIBLE
========================================
```

---

## 🔮 Future Improvements

- Add support for saving student reports to a text file or CSV export.
- Support batch processing for multiple students at once.
- Add chart visualization for attendance breakdown.
