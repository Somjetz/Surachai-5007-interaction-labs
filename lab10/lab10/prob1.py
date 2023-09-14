import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from lab8.prob2 import MenuBar

class ToolbarIcons(MenuBar):
    def __init__(self):
        super(ToolbarIcons, self).__init__()
        self.setWindowTitle("Calculator with menus and Toolbar")
        self._addAction()
        self._addToolbar()

    def _addAction(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.saveAction.setIcon(QIcon("images/file-save.png"))
        self.openAction.setIcon(QIcon("images/file-open.svg"))
        self.clearAction.setIcon(QIcon("images/edit-clear.png"))

    def _addToolbar(self):
        fileToolbar = QToolBar('iconbar')
        self.addToolBar(fileToolbar)
        fileToolbar.addAction(self.openAction)
        fileToolbar.addAction(self.saveAction)
        fileToolbar.addAction(self.clearAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolbarIcons()
    window.show()
    app.exec()
