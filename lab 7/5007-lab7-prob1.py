import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt

class NameForm(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Name Form')

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('First Name:'), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)

        layout.addWidget(QLabel('Last Name:'), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)

        submit_button = QPushButton('Submit')
        submit_button.setStyleSheet("color: green;")
        layout.addWidget(submit_button, 3, 1, alignment=Qt.AlignmentFlag.AlignRight)

        cancel_button = QPushButton('Cancel')
        cancel_button.setStyleSheet("color: red;")
        cancel_button.clicked.connect(QApplication.quit)  # Connect to quit method
        layout.addWidget(cancel_button, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameForm()
    sys.exit(app.exec())
