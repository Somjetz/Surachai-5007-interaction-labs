import sys
import os
from PyQt6.QtWidgets import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from lab10.prob2 import Shortcut

class MessageBoxDisplay(Shortcut):
    def __init__(self):
        super(MessageBoxDisplay, self).__init__()
        self.setWindowTitle("Calculator with Message Box")
        self.line_edit1.returnPressed.connect(self.checkinput)
        self.line_edit2.returnPressed.connect(self.checkinput)
        
    def checkinput(self):
        if self.line_edit1.text().isdigit() == False:
            QMessageBox.warning(self, "", "Please enter the first number")

        elif self.line_edit2.text().isdigit() == False:
            QMessageBox.warning(self, "", "Please enter the second number")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MessageBoxDisplay()
    window.show()
    app.exec()