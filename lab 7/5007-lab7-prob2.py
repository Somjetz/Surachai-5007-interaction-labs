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

        font = QFont("Arial", 20)  # SET Font size 20

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

    def on_button_click(self, text):
        current_text = self.output_label.text()
        new_text = current_text + text
        self.output_label.setText(new_text)

app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())