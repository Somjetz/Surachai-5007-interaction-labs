class ComEnStudent:
    def __init__(self, name, courses=None):
        self.name = name
        self.courses = courses if courses is not None else []

    def take_courses(self, *courses):
        self.courses.extend(courses)

    def __str__(self):
        courses_str = ', '.join([f"'{course}'" for course in self.courses])
        return f"{self.name} has taken these courses: [{courses_str}]"

class CoEStudent(ComEnStudent):
    def __init__(self, name, courses=None):
        super().__init__(name, courses)

class DMEStudent(ComEnStudent):
    def __init__(self, name, courses=None):
        super().__init__(name, courses)
        self.content_type = None

    def make_content_type(self, content_type):
        self.content_type = content_type

    def __str__(self):
        content_info = f", Specialize in creating content type: [{self.content_type}]" if self.content_type else ""
        return f"{super().__str__()}\n{content_info}"

if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("Sc401206")
        print(com_student)