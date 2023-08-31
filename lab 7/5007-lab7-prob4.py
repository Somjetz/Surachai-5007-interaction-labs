import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        font = QFont("Arial", 20)  # Set font size 20

        for pos, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            button.setFont(font)
            button.clicked.connect(lambda checked, text=name: self.on_button_click(text))
            grid.addWidget(button, *pos)

        self.output_label = QLabel()
        self.output_label.setFont(font)
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.output_label.setStyleSheet("background-color: yellow; color: black;")
        grid.addWidget(self.output_label, 0, 0, 1, 4)

        self.move(300, 150)

        self.current_input = ''
        self.first_operand = ''
        self.operator = ''

    def on_button_click(self, text):
        if text.isdigit():
            self.current_input += text
            self.output_label.setText(self.current_input)
        elif text in ['+', '-', '*', '/']:
            if self.current_input:
                self.first_operand = self.current_input
                self.operator = text
                self.current_input = ''
        elif text == '=':
            if self.current_input and self.first_operand and self.operator:
                try:
                    second_operand = self.current_input
                    result = self.calculate_result(int(self.first_operand), int(second_operand))
                    self.output_label.setText(str(result))
                except Exception as e:
                    self.output_label.setText("Error")
            self.current_input = ''
            self.first_operand = ''
            self.operator = ''

    def calculate_result(self, a, b):
        if self.operator == '+':
            return a + b
        elif self.operator == '-':
            return a - b
        elif self.operator == '*':
            return a * b
        elif self.operator == '/':
            if b != 0:
                return a / b
            else:
                return "Error"

app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
