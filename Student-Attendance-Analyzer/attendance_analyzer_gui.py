"""
Student Attendance Analyzer - GUI Version

A modern, beginner-friendly Tkinter GUI application for analyzing student
attendance percentage, absent days, and exam eligibility status.
"""

import tkinter as tk
from tkinter import messagebox

# Color Palette Design Tokens
PRIMARY_COLOR = "#4F46E5"      # Indigo-600 (Header / Primary Button)
SECONDARY_COLOR = "#6366F1"    # Indigo-500 (Hover state)
BG_COLOR = "#F8FAFC"           # Slate-50 (Window background)
CARD_BG = "#FFFFFF"            # White (Card containers)
TEXT_MAIN = "#0F172A"          # Slate-900 (Main text)
TEXT_MUTED = "#64748B"         # Slate-500 (Secondary text)
SUCCESS_COLOR = "#16A34A"      # Green-600 (Eligible status)
ERROR_COLOR = "#DC2626"        # Red-600 (Not eligible status / errors)
BORDER_COLOR = "#E2E8F0"       # Slate-200 (Borders)


def calculate_attendance_metrics(total_working_days: int, present_days: int):
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


class AttendanceAnalyzerGUI:
    """Tkinter Application class for Student Attendance Analyzer GUI."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Student Attendance Analyzer")
        self.root.geometry("500x640")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        # Header Section
        header_frame = tk.Frame(self.root, bg=PRIMARY_COLOR, pady=18)
        header_frame.pack(fill="x", side="top")

        title_label = tk.Label(
            header_frame,
            text="Student Attendance Analyzer",
            font=("Helvetica", 16, "bold"),
            fg="#FFFFFF",
            bg=PRIMARY_COLOR,
        )
        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text="Check exam eligibility & attendance summary",
            font=("Helvetica", 10),
            fg="#E0E7FF",
            bg=PRIMARY_COLOR,
        )
        subtitle_label.pack(pady=(2, 0))

        # Main Form Container Card
        form_card = tk.Frame(
            self.root,
            bg=CARD_BG,
            highlightbackground=BORDER_COLOR,
            highlightthickness=1,
            padx=20,
            pady=15,
        )
        form_card.pack(fill="x", padx=20, pady=(15, 10))

        def create_input_field(parent, label_text):
            label = tk.Label(
                parent,
                text=label_text,
                font=("Helvetica", 9, "bold"),
                fg=TEXT_MAIN,
                bg=CARD_BG,
                anchor="w",
            )
            label.pack(fill="x", pady=(6, 2))

            entry = tk.Entry(
                parent,
                font=("Helvetica", 10),
                fg=TEXT_MAIN,
                bg="#F8FAFC",
                relief="flat",
                highlightthickness=1,
                highlightbackground=BORDER_COLOR,
                highlightcolor=PRIMARY_COLOR,
            )
            entry.pack(fill="x", ipady=5, pady=(0, 2))
            return entry

        self.name_entry = create_input_field(form_card, "Student Name")
        self.reg_entry = create_input_field(form_card, "Register Number")
        self.working_days_entry = create_input_field(form_card, "Total Working Days")
        self.present_days_entry = create_input_field(form_card, "Present Days")

        # Action Buttons Container
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(fill="x", padx=20, pady=5)

        calc_btn = tk.Button(
            btn_frame,
            text="Calculate Attendance",
            font=("Helvetica", 10, "bold"),
            fg="#FFFFFF",
            bg=PRIMARY_COLOR,
            activebackground=SECONDARY_COLOR,
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.on_calculate,
            pady=7,
        )
        calc_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        reset_btn = tk.Button(
            btn_frame,
            text="Reset",
            font=("Helvetica", 10, "bold"),
            fg=TEXT_MAIN,
            bg="#E2E8F0",
            activebackground="#CBD5E1",
            activeforeground=TEXT_MAIN,
            relief="flat",
            cursor="hand2",
            command=self.on_reset,
            pady=7,
            width=10,
        )
        reset_btn.pack(side="right", padx=(5, 0))

        # Result Summary Card Container
        self.result_card = tk.Frame(
            self.root,
            bg=CARD_BG,
            highlightbackground=BORDER_COLOR,
            highlightthickness=1,
            padx=20,
            pady=15,
        )
        self.result_card.pack(fill="x", padx=20, pady=(10, 15))

        tk.Label(
            self.result_card,
            text="Attendance Report",
            font=("Helvetica", 11, "bold"),
            fg=TEXT_MAIN,
            bg=CARD_BG,
        ).pack(anchor="w", pady=(0, 6))

        # Report Detail Reactive StringVars
        self.name_res_var = tk.StringVar(value="Student: -")
        self.reg_res_var = tk.StringVar(value="Register No: -")
        self.days_summary_var = tk.StringVar(
            value="Working Days: - | Present: - | Absent: -"
        )
        self.percentage_var = tk.StringVar(value="Attendance: -")

        tk.Label(
            self.result_card,
            textvariable=self.name_res_var,
            font=("Helvetica", 10, "bold"),
            fg=TEXT_MAIN,
            bg=CARD_BG,
        ).pack(anchor="w")

        tk.Label(
            self.result_card,
            textvariable=self.reg_res_var,
            font=("Helvetica", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG,
        ).pack(anchor="w", pady=(1, 4))

        tk.Label(
            self.result_card,
            textvariable=self.days_summary_var,
            font=("Helvetica", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG,
        ).pack(anchor="w", pady=(0, 4))

        tk.Label(
            self.result_card,
            textvariable=self.percentage_var,
            font=("Helvetica", 13, "bold"),
            fg=PRIMARY_COLOR,
            bg=CARD_BG,
        ).pack(anchor="w", pady=(0, 6))

        # Status Pill Label
        self.status_label = tk.Label(
            self.result_card,
            text="STATUS: -",
            font=("Helvetica", 10, "bold"),
            fg=TEXT_MUTED,
            bg="#F1F5F9",
            padx=10,
            pady=3,
        )
        self.status_label.pack(anchor="w")

    def on_calculate(self):
        """Validate inputs, perform calculations, and render the result section."""
        name = self.name_entry.get().strip()
        reg_no = self.reg_entry.get().strip()
        working_days_str = self.working_days_entry.get().strip()
        present_days_str = self.present_days_entry.get().strip()

        # Input Validation Checks
        if not name:
            messagebox.showerror("Input Error", "Student Name cannot be empty.")
            self.name_entry.focus()
            return

        if not reg_no:
            messagebox.showerror("Input Error", "Register Number cannot be empty.")
            self.reg_entry.focus()
            return

        try:
            working_days = int(working_days_str)
        except ValueError:
            messagebox.showerror(
                "Input Error", "Total Working Days must be a valid whole number."
            )
            self.working_days_entry.focus()
            return

        if working_days <= 0:
            messagebox.showerror(
                "Input Error", "Total Working Days must be greater than 0."
            )
            self.working_days_entry.focus()
            return

        try:
            present_days = int(present_days_str)
        except ValueError:
            messagebox.showerror(
                "Input Error", "Present Days must be a valid whole number."
            )
            self.present_days_entry.focus()
            return

        if present_days < 0:
            messagebox.showerror("Input Error", "Present Days cannot be negative.")
            self.present_days_entry.focus()
            return

        if present_days > working_days:
            messagebox.showerror(
                "Input Error",
                f"Present Days ({present_days}) cannot be greater than Total Working Days ({working_days}).",
            )
            self.present_days_entry.focus()
            return

        # Perform Calculation
        absent_days, percentage, status = calculate_attendance_metrics(
            working_days, present_days
        )

        # Render Results
        self.name_res_var.set(f"Student: {name}")
        self.reg_res_var.set(f"Register No: {reg_no}")
        self.days_summary_var.set(
            f"Working: {working_days} | Present: {present_days} | Absent: {absent_days}"
        )
        self.percentage_var.set(f"Attendance: {percentage:.2f}%")

        if status == "ELIGIBLE":
            self.status_label.config(
                text="Status: ELIGIBLE", fg="#FFFFFF", bg=SUCCESS_COLOR
            )
        else:
            self.status_label.config(
                text="Status: NOT ELIGIBLE", fg="#FFFFFF", bg=ERROR_COLOR
            )

    def on_reset(self):
        """Clear all inputs and reset the result summary display."""
        self.name_entry.delete(0, tk.END)
        self.reg_entry.delete(0, tk.END)
        self.working_days_entry.delete(0, tk.END)
        self.present_days_entry.delete(0, tk.END)

        self.name_res_var.set("Student: -")
        self.reg_res_var.set("Register No: -")
        self.days_summary_var.set("Working Days: - | Present: - | Absent: -")
        self.percentage_var.set("Attendance: -")
        self.status_label.config(text="STATUS: -", fg=TEXT_MUTED, bg="#F1F5F9")
        self.name_entry.focus()


def main():
    root = tk.Tk()
    app = AttendanceAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
