import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from prob1 import CalculatorApp

class MenuBar(CalculatorApp):
    def __init__(self):
        super(MenuBar, self).__init__()
        self.setWindowTitle("Calculator with menus")
        self._addMenus()
        self._handleMenus()

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
        self.clearAction = QAction("Clear", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        
        self.editMenu.addAction(self.clearAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)

    def _addConfigMenu(self):
        self.colorAction = QAction("Color", self)
        self.sizeAction = QAction("Size", self)
        
        self.configMenu.addAction(self.colorAction)
        self.configMenu.addAction(self.sizeAction)

    def _handleMenus(self):
        self.saveAction.triggered.connect(self._handleSaveMenus)
        self.openAction.triggered.connect(self._handleOpenMenus)
        self.exitAction.triggered.connect(self._handleExitMenus)
        self.clearAction.triggered.connect(self._handleClearMenus)

    def _handleSaveMenus(self):
        reply = QMessageBox.information(self, '',
                                     "Writing result to file result.txt",
                                     
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Ok)
        if reply == QMessageBox.StandardButton.Ok:
            with open("result.txt", "w") as f:
                f.write(self.result_text.toPlainText())

    def _handleOpenMenus(self):
        reply = QMessageBox.information(self, '',
                                     "Reading result from file result.txt",
                                     
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Ok)
        if reply == QMessageBox.StandardButton.Ok:
            with open("result.txt", "r") as f:
                self.result_text.setText(f.read())

    def _handleExitMenus(self):
        sys.exit()

    def _handleClearMenus(self):
        self.line_edit1.clear()
        self.line_edit2.clear()
        self.result_text.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuBar()
    window.show()
    sys.exit(app.exec())