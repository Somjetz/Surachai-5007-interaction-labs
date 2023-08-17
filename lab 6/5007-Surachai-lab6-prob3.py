import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, name, id):
        super(MainWindow, self).__init__()

        self.setWindowTitle("653040500-7")

        self.name = name
        self.student_id = id

        layout = QVBoxLayout()

        label = QLabel("\nSurachai Visetla\n", self)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.button = QPushButton('Quit', self)
        self.button.setToolTip('Are you sure you want to quit?')
        self.button.clicked.connect(self.quit_clicked)

        layout.addWidget(label)
        layout.addWidget(self.button)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmation', "Are you sure you want to quit?",
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def quit_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    student = {"name": "Surachai Visetla", "id": "653040500-7"}

    window = MainWindow(student["name"], student["id"])
    window.show()

    sys.exit(app.exec())