import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QKeySequence
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from lab10.prob1 import ToolbarIcons

class Shortcut(ToolbarIcons):
    def __init__(self):
        super(Shortcut, self).__init__()
        self.setWindowTitle("Calculator with Status and Shortcut")

        self._addShortcut()

    def _addShortcut(self):
        
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready")

        self.openAction.setStatusTip("Open File")
        self.saveAction.setStatusTip("Save File")
        self.clearAction.setStatusTip("Clear File")
        self.exitAction.setStatusTip("Exit the application")


        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.clearAction.setShortcut(QKeySequence("Ctrl+R"))
        self.exitAction.setShortcut(QKeySequence("Ctrl+Q"))
        self.exitAction.triggered.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Shortcut()
    window.show()
    app.exec()