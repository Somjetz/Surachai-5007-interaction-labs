class Person:
    def __stats__(self, name, age, email, occupation):
        self.name = name
        self.age = age
        self.email = email
        self.occupation = occupation

    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Occupation:", self.occupation)


if __name__ == "__main__":
    person1 = Person("John Doe", 30, "john.doe@example.com", "Engineer")
    person1.display_information()
    
    person2 = Person("Jaw Maw", 24, "APOHFDP(@gmail.com)", "Encyocopedia" )
    person2.display_information()