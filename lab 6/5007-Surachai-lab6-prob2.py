import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class UserInfoApp(QWidget):
    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('User Info App')

        self.name_label = QLabel('Enter your text:')
        self.text_input = QLineEdit()
        self.text_input.textChanged.connect(self.update_output_label)

        self.output_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def update_output_label(self):
        user_text = self.text_input.text()
        user_info_text = f"{user_text}, {self.user_info['name']} {self.user_info['id']}"
        self.output_label.setText(user_info_text)

if __name__ == '__main__':
    user_info = {
        'name': 'Surachai',
        'id': '500-7'
    }

    app = QApplication(sys.argv)
    window = UserInfoApp(user_info)
    window.show()
    sys.exit(app.exec())