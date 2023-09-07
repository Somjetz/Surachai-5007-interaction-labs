import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.helpMenu = self.menuBar.addMenu("config")

    def initUI(self):
        # Create the main window
        self.setWindowTitle('Calculator App')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create the grid layout for input and buttons
        grid_layout = QGridLayout()

        # Labels
        label1 = QLabel('Enter the first number:')
        label2 = QLabel('Enter the second number:')
        label_result = QLabel('Result:')

        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(label2, 1, 0)

        # Line Edits
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()

        self.line_edit1.setStyleSheet("background-color: yellow;")
        self.line_edit2.setStyleSheet("background-color: yellow;")

        grid_layout.addWidget(self.line_edit1, 0, 1)
        grid_layout.addWidget(self.line_edit2, 1, 1)

        layout.addLayout(grid_layout)

        # Operator Buttons
        operator_layout = QHBoxLayout()

        btn_add = QPushButton('+')
        btn_subtract = QPushButton('-')
        btn_multiply = QPushButton('*')
        btn_divide = QPushButton('/')

        # Connect buttons to calculation functions
        btn_add.clicked.connect(lambda: self.calculate('+'))
        btn_subtract.clicked.connect(lambda: self.calculate('-'))
        btn_multiply.clicked.connect(lambda: self.calculate('*'))
        btn_divide.clicked.connect(lambda: self.calculate('/'))

        operator_layout.addWidget(btn_add)
        operator_layout.addWidget(btn_subtract)
        operator_layout.addWidget(btn_multiply)
        operator_layout.addWidget(btn_divide)

        layout.addLayout(operator_layout)

        # Result Label and Text Edit
        result_layout = QHBoxLayout()

        label_result = QLabel('Result:')
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: cadetblue;")

        result_layout.addWidget(label_result)
        result_layout.addWidget(self.result_text)

        layout.addLayout(result_layout)

        # Create Menus
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        config_menu = menubar.addMenu('Config')

    def calculate(self, operator):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        if operator == '/' and num2 == 0:
            self.result_text.append('Error: Division by zero')
        else:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            else:  # operator == '/'
                result = num1 / num2
            self.result_text.append(f"{num1} {operator} {num2} = {result}")

    def clear_result(self):
        self.result_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec())
