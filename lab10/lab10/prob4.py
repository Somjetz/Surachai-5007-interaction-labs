import sys, os
from PyQt6.QtWidgets import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from lab10.prob3 import MessageBoxDisplay

class CalculatorFileDialog(MessageBoxDisplay):
    def __init__(self):
        super(CalculatorFileDialog, self).__init__()
        self.setWindowTitle("Calculator with File Dialog")
        self.path = os.path.dirname(__file__)
        os.chdir(self.path)

    def _handleOpenMenus(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', self.path)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.result_text.setText(data)

    def _handleSaveMenus(self):
        fname = QFileDialog.getSaveFileName(self, 'SaveFile', self.path)
        if fname[0]:
            with open(fname[0], 'w') as file:
                file.write(self.result_text.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorFileDialog()
    window.show()
    sys.exit(app.exec())


