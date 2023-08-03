class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage
        
    def set_speed(self, speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed
    
    def __str__(self):
        return f"Name: {self.name} speed: {self.__speed} mileage: {self.mileage}"
        
class Car(Vehicle):
    def __init__(self, num_doors, name, speed, mileage):
        super().__init__(name, speed, mileage)
        self.num_doors = num_doors
        
    def __str__(self):
        return f"Name: {self.name} speed: {self.get_speed()} mileage: {self.mileage}, num doors: {self.num_doors}"

class Bus(Vehicle):
    def __init__(self, capacity, name, speed, mileage):
        super().__init__(name, speed, mileage)
        self.capacity = capacity
    
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def __str__(self):
        return f"Name: {self.name} speed: {self.get_speed()} mileage: {self.mileage}, capacity: {self.capacity}"
    
if __name__ == "__main__":
    car = Car(4, "Toyota Vios", 90, 150000)
    bus = Bus(100, "School Volvo", 12, 200000)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)