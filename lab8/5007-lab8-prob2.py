import sys
from PyQt6.QtWidgets import QApplication, QToolBar, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from prob1 import CalculatorApp

class MenuBar(CalculatorApp):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with menus")
        self.resize(400, 200)

    def _createMenuBar(self):
        self.fileMenu = self.menuBar().addMenu("File")
        self.editMenu = self.menuBar().addMenu("Edit")
        self.configMenu = self.menuBar().addMenu("Config")

    def _createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.editToolbar = QToolBar("Edit", self)
        self.addToolBar(self.editToolbar)
        ConfigToolBar = QToolBar("Color", self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, ConfigToolBar)

    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addConfigMenu()

    def _addFileMenu(self):
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)

        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

    def _addEditMenu(self):
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.clearAction = QAction("Clear", self)  # Add Clear action to the Edit menu

        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.clearAction)  # Add Clear action to the Edit menu

        # Connect the Clear action to the clear function
        self.clearAction.triggered.connect(self.clear)

    def clear(self):
        # Add logic to clear the calculator or text fields here
        pass

    def _addConfigMenu(self):
        self.aboutAction = QAction("color", self)
        self.configMenu.addAction(self.aboutAction)
        self.aboutAction = QAction("Size", self)
        self.configMenu.addAction(self.aboutAction)

app = QApplication(sys.argv)
window = MenuBar()
window.show()
app.exec()