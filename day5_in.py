class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) #calling the parent class constructor
        self.breed = breed
    def speak(self): #overridding the speak method
        print("Woof Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def speak(self):
        print("Meow Meow!")

class Bird(Animal): #already inherites the name from animal
    def speak(self):
        print("Chirp Chirp!")

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Black")
my_bird = Bird("Tweety")

# my_dog.speak()
# my_cat.speak()
# my_bird.speak()

animals = [my_dog, my_cat, my_bird] #list of objects
for animal in animals:
    animal.speak()