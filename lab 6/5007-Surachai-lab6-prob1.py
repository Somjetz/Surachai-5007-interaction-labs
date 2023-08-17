import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self,student_name, student_id):
        super().__init__()
        self.student_name = student_name
        self.student_id = student_id

        # self = make it worldwide
        self.button_is_checked = True

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.clicked_button)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)
    # self
    def clicked_button(self):
        self.button.setText(self.student_id)
        self.button.setWindowTitle(self.student_id)
        self.button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    student = {"name": "Surachai", "id": "653040500-7"}

    window = MainWindow(student["name"], student["id"])
    window.show()
    app.exec()