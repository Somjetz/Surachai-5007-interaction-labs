import sys, os
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from lab10.prob4 import CalculatorFileDialog

class ColorDialog(CalculatorFileDialog):
    def __init__(self):
        super(ColorDialog, self).__init__()
        self.setWindowTitle("Calculator with Dialog")
        self.colorAction.triggered.connect(self.setColor)
        self.sizeAction.triggered.connect(self.setFont)
    
    def setColor(self):
        color_result_background = QColorDialog.getColor()
        if color_result_background.isValid():
            bg_color = color_result_background.name()
            text_color = 'black' if color_result_background.lightness() < 128 else 'white'
        
        self.result_text.setStyleSheet(f"background-color: {bg_color}; color: {text_color};")

    def setFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_text.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorDialog()
    window.show()
    sys.exit(app.exec())