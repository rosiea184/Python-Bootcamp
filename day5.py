class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def start(self):
        print(f"The {self.color} {self.brand} car has started")

myCar = Car("Toyota", "red")
myCar.start()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

person1 = Person("Alice", 30)
person1.introduce()