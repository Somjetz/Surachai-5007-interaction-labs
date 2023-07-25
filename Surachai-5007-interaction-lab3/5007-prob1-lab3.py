class Teacher:
    def __init__(self, name, office_no, research_work, *course_work):
        self.name = name
        self.office_no = office_no
        self.research_work = research_work
        self.course_work = course_work

    def print_office_no(self):
        print("Office Number:", self.office_no)

    def print_research_work(self):
        print("Research Work:", self.research_work)

    def print_course_work(self):
        print("Course Work:")
        for course in self.course_work:
            print(course)

if __name__ == "__main__":
    manee = Teacher("Manee", "Rm. 4203", "Artificial Intelligence", "EN842004", "EN813701")
    mana = Teacher("Mana", "Rm. 4209", "Internet of Things", "EN842005", "EN813703")

    manee.print_office_no()
    manee.print_research_work()
    manee.print_course_work()

    mana.print_office_no()
    mana.print_research_work()
    mana.print_course_work()