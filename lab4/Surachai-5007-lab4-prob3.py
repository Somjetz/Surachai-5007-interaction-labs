class Pet:
    def __init__(self, name, owner=None, color=None):
        self.name = name
        self.owner = owner
        self.color = color
        
    def show_info(self):
        print(f"I'm {self.name}")
        if self.color:
            print(f" and is {self.color}")
        if self.owner:
            print(f" belonging to {self.owner}")
        
    def move(self):
        print(f"Moving . . .")

class Cat(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name, owner, color)
        
    def move(self):
        print("Cat likes to walk more than run")

class Dog(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name, owner, color)
        
    def move(self):
        print("Dog likes to run more than walk")
        
    def eat_cat(self, cat):
        print(f"Dog {self.name} eats cat {cat.name}")

if __name__ == "__main__":
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()

    cat1 = Cat("Thongdee", "Manee", "white")
    cat1.show_info()
    cat1.move()

    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)