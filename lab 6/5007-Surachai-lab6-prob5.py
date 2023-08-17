import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QListWidget, QVBoxLayout

class CourseSelectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Course Selection App')

        self.name_label = QLabel('Enter your name:')
        self.name_input = QLineEdit()

        self.course_list = QListWidget()
        self.course_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.course_list.addItems(["EN842300", "EN842314", "EN842315"])
        self.course_list.itemClicked.connect(self.display_selected_courses)  # Connect itemClicked to display_selected_courses

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.course_list)

        self.setLayout(layout)

        self.output_label = QLabel()  # Create a label for displaying the output
        layout.addWidget(self.output_label)  # Add the output label to the layout

    def display_selected_courses(self, item):
        name = self.name_input.text()
        selected_courses = [selected_item.text() for selected_item in self.course_list.selectedItems()]

        if name and selected_courses:
            course_text = ", ".join(selected_courses)
            message = f"Hello {name}! You are interested in these courses: {course_text}"
            self.output_label.setText(message)  # Update the output label text
            self.output_label.setStyleSheet('background-color: yellow; color: black')  # Set yellow background and black text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CourseSelectionApp()
    window.show()
    sys.exit(app.exec())