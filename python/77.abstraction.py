from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n

    @abstractmethod
    def start(self):
        pass  # Must be implemented in child classes

    def display(self):
        print("Hi, I am calling from Vehicle class")


# Concrete class: Bike
class Bike(Vehicle):
    def __init__(self, n,colour):
        super().__init__(n)  # Proper way to call parent constructor
        self.colour=colour
        
    def start(self):
        print("Bike starts with a kick")
        
    def display(self):
        print(f" the colour of the bike is {self.colour}")

# Concrete class: Scooty
class Scooty(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start(self):
        print("Scooty starts with self-start")


# Concrete class: Car
class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start(self):
        print("Car starts with push-button")


# ❌ This is NOT allowed:
# v = Vehicle()  # Will raise an error because 'start' is abstract

# ✅ Create objects of subclasses
b = Bike(2,"black")
s = Scooty(2)
c = Car(4)

# Calling methods
b.start()     # Output: Bike starts with a kick
s.start()     # Output: Scooty starts with self-start
c.start()     # Output: Car starts with push-button

b.display()
s.display()# Output: Hi, I am calling from Vehicle class
print(b.no_of_tyres)  # Output: 2
