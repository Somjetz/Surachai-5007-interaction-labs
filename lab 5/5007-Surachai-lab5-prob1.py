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

#Instance of Classes
human = Human()
snake = Snake()
dog = Dog()

#Call function like a print
human.move()
snake.move()
dog.move()