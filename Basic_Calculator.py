"""
A desktop basic calculator implemented with Python and Tkinter.

Original author: Parashar Bhatt
"""

import os
import math
import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.resizable(False, False)
        self.configure(padx=18, pady=18)

        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "HandDrawCalculator.ico")
        if os.name == "nt" and os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        self.current_value = "0"
        self.pending_value = None
        self.pending_operator = None
        self.waiting_for_operand = False
        self.last_operator = None
        self.last_operand = None

        self._create_style()
        self._create_widgets()
        self._bind_keys()

    def _create_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Calculator.TFrame", background="#eef2f6")
        style.configure("Display.TEntry",
                        fieldbackground="#ffffff",
                        foreground="#20242a",
                        padding=(14, 12),
                        borderwidth=0)
        style.configure("Number.TButton", font=("Segoe UI", 12), padding=(10, 12))
        style.configure("Operator.TButton", font=("Segoe UI", 12, "bold"),
                        foreground="#1167b1", padding=(10, 12))
        style.configure("Action.TButton", font=("Segoe UI", 12),
                        foreground="#b42318", padding=(10, 12))

        self.configure(background="#eef2f6")

    def _create_widgets(self):
        frame = ttk.Frame(self, style="Calculator.TFrame")
        frame.grid(row=0, column=0)

        self.display_variable = tk.StringVar(value="0")
        self.display = ttk.Entry(
            frame,
            textvariable=self.display_variable,
            justify="right",
            width=18,
            font=("Segoe UI", 22),
            style="Display.TEntry",
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 12), ipady=10)

        buttons = (
            ("C", "Action.TButton", self.clear, 1, 0),
            ("Back", "Action.TButton", self.backspace, 1, 1),
            ("%", "Operator.TButton", self.percent, 1, 2),
            ("/", "Operator.TButton", lambda: self.choose_operator("/"), 1, 3),
            ("7", "Number.TButton", lambda: self.input_digit("7"), 2, 0),
            ("8", "Number.TButton", lambda: self.input_digit("8"), 2, 1),
            ("9", "Number.TButton", lambda: self.input_digit("9"), 2, 2),
            ("*", "Operator.TButton", lambda: self.choose_operator("*"), 2, 3),
            ("4", "Number.TButton", lambda: self.input_digit("4"), 3, 0),
            ("5", "Number.TButton", lambda: self.input_digit("5"), 3, 1),
            ("6", "Number.TButton", lambda: self.input_digit("6"), 3, 2),
            ("-", "Operator.TButton", lambda: self.choose_operator("-"), 3, 3),
            ("1", "Number.TButton", lambda: self.input_digit("1"), 4, 0),
            ("2", "Number.TButton", lambda: self.input_digit("2"), 4, 1),
            ("3", "Number.TButton", lambda: self.input_digit("3"), 4, 2),
            ("+", "Operator.TButton", lambda: self.choose_operator("+"), 4, 3),
            ("+/-", "Number.TButton", self.toggle_sign, 5, 0),
            ("0", "Number.TButton", lambda: self.input_digit("0"), 5, 1),
            (".", "Number.TButton", self.input_decimal, 5, 2),
            ("=", "Operator.TButton", self.calculate, 5, 3),
            ("x^2", "Operator.TButton", self.square, 6, 0),
            ("x^y", "Operator.TButton", lambda: self.choose_operator("^"), 6, 1),
        )

        for text, style_name, command, row, column in buttons:
            button = ttk.Button(frame, text=text, style=style_name, command=command)
            button.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)

        for column in range(4):
            frame.columnconfigure(column, weight=1, uniform="column")
        for row in range(1, 7):
            frame.rowconfigure(row, weight=1)

    def _bind_keys(self):
        for number in "0123456789":
            self.bind(number, lambda event, digit=number: self.input_digit(digit))
        for operator in "+-*/":
            self.bind(operator, lambda event, op=operator: self.choose_operator(op))
        self.bind("^", lambda event: self.choose_operator("^"))
        self.bind(".", self.input_decimal)
        self.bind("<Return>", lambda event: self.calculate())
        self.bind("<KP_Enter>", lambda event: self.calculate())
        self.bind("<BackSpace>", lambda event: self.backspace())
        self.bind("<Escape>", lambda event: self.clear())
        self.bind("<Delete>", lambda event: self.clear())

    def _set_display(self, value):
        self.current_value = value
        self.display_variable.set(value)

    @staticmethod
    def _format_number(value):
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            return "Error"
        if abs(value) < 1e-12:
            value = 0.0
        text = format(value, ".12g")
        return text

    def input_digit(self, digit):
        if self.current_value == "Error" or self.waiting_for_operand:
            self._set_display(digit)
            self.waiting_for_operand = False
        elif self.current_value == "0":
            self._set_display(digit)
        else:
            if len(self.current_value.replace("-", "").replace(".", "")) >= 16:
                return
            self._set_display(self.current_value + digit)

    def input_decimal(self, event=None):
        if self.current_value == "Error" or self.waiting_for_operand:
            self._set_display("0.")
            self.waiting_for_operand = False
        elif "." not in self.current_value:
            self._set_display(self.current_value + ".")

    def toggle_sign(self):
        if self.current_value == "0" or self.current_value == "Error":
            return
        if self.current_value.startswith("-"):
            self._set_display(self.current_value[1:])
        else:
            self._set_display("-" + self.current_value)

    def backspace(self):
        if self.current_value == "Error" or self.waiting_for_operand:
            self._set_display("0")
            return
        updated = self.current_value[:-1]
        self._set_display(updated if updated not in ("", "-", "-0") else "0")

    def clear(self):
        self._set_display("0")
        self.pending_value = None
        self.pending_operator = None
        self.waiting_for_operand = False
        self.last_operator = None
        self.last_operand = None

    def percent(self):
        if self.current_value == "Error":
            return
        value = float(self.current_value) / 100
        self._set_display(self._format_number(value))

    def choose_operator(self, operator):
        if self.current_value == "Error":
            return

        value = float(self.current_value)
        if self.pending_operator and not self.waiting_for_operand:
            value = self._perform_operation(self.pending_value, value, self.pending_operator)
            if value == "Error":
                self._set_display("Error")
                self.pending_value = None
                self.pending_operator = None
                return
            self._set_display(value)

        self.pending_value = float(self.current_value)
        self.pending_operator = operator
        self.waiting_for_operand = True

    def calculate(self):
        if self.pending_operator is not None:
            if self.current_value == "Error":
                return
            if self.waiting_for_operand:
                second_value = self.pending_value
            else:
                second_value = float(self.current_value)
            first_value = self.pending_value
            operator = self.pending_operator
        elif self.last_operator is not None and self.last_operand is not None:
            first_value = float(self.current_value)
            second_value = self.last_operand
            operator = self.last_operator
        else:
            return

        result = self._perform_operation(
            first_value,
            second_value,
            operator,
        )
        if result == "Error":
            self._set_display("Error")
        else:
            self._set_display(result)

        self.last_operator = operator
        self.last_operand = second_value
        self.pending_value = None
        self.pending_operator = None
        self.waiting_for_operand = True

    def square(self):
        if self.current_value == "Error":
            return
        value = float(self.current_value)
        try:
            result = value ** 2
            self._set_display(self._format_number(result))
        except OverflowError:
            self._set_display("Error")
        self.waiting_for_operand = True

    def _perform_operation(self, first, second, operator):
        try:
            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/":
                if second == 0:
                    return "Error"
                result = first / second
            elif operator == "^":
                result = first ** second
            else:
                return "Error"
            return self._format_number(result)
        except (OverflowError, ZeroDivisionError, TypeError, ValueError):
            return "Error"


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
