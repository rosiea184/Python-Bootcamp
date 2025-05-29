# Design a Vehicle class with subclasses Car and Bike, each with unique attributes and behaviors.

class Vehicle:
    def __init__(self, wheels, make):
        self.wheels = wheels
        self.make = make
    
class Car(Vehicle):
    def __init__(self, wheels, make, color):
        super().__init__(wheels, make)
        self.wheels = 4
        self.color = color
    def display_info(self):
        print(f"Car Make: {self.make}, Wheels: {self.wheels}, Color: {self.color}")

class Bike(Vehicle):
    def __init__(self, wheels, make, style):
        super().__init__(wheels, make)
        self.wheels = 2
        self.style = style
    def display_info(self):
        print(f"Bike Make: {self.make}, Wheels: {self.wheels}")

honda = Car(2,"Honda", "green")
honda.display_info()

# Define a BankAccount class with attributes balance and methods deposit and withdraw.
# Create a subclass SavingsAccount with an additional method add_interest.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print(f"Your balance is {self.balance}")
    def withdraw(self, money):
        if money <= self.balance:
            self.balace -= money
        else:
            print("Withdraw amount is larger than account balance")
        print(f"Your balance is {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest):
        super().__init__(balance)
        self.interest = interest
    def deposit(self, money):
        return super().deposit(money)
    def withdraw(self, money):
        return super().withdraw(money)
    def add_interest(self):
        self.balance += self.balance * self.interest
        return self.balance