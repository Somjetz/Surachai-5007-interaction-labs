from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

if __name__ == "__main__":
    #Instance of Classes
    human = Human()
    snake = Snake()
    dog = Dog()

    print("Documentation for Animal class:\n", Animal.__doc__)
    print("\nDocumentation for Human class:\n", Human.__doc__)
    print("\nDocumentation for Snake class:\n", Snake.__doc__)
    print("\nDocumentation for Dog class:\n", Dog.__doc__)

    print("\nDocumentation for move method in Human:\n", Human.move.__doc__)
    print("\nDocumentation for move method in Snake:\n", Snake.move.__doc__)
    print("\nDocumentation for move method in Dog:\n", Dog.move.__doc__)

    #Call function like a print
    human.move()
    snake.move()
    dog.move()