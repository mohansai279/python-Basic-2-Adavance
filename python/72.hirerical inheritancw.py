# 🧱 Base Class: Human
class Human:
    def __init__(self, name, age):
        # Initialize common attributes for all humans
        self.name = name
        self.age = age

    def showDetails(self):
        # Display the name and age
        print(f"Name: {self.name}, Age: {self.age}")

    def eat(self):
        # Common behavior: all humans can eat
        print("I can eat")

# 👨‍🦰 Derived Class: Male inherits from Human
class Male(Human):
    def __init__(self, name, age, location):
        # Initialize the base class using super() to avoid repeating code
        super().__init__(name, age)
        # Add an additional attribute specific to Male
        self.location = location

    def sleep(self):
        # Behavior specific to Male
        print("I can sleep whole day")

# 👩 Derived Class: Female inherits from Human
class Female(Human):
    def work(self):
        # Behavior specific to Female
        print("I can code")


# 🚀 Creating an object of Female
female_1 = Female("Jiya", 20)  # name = Jiya, age = 20

# 🔹 Calling inherited method from Human
female_1.eat()  # Output: I can eat

# 🔹 Calling Female-specific method
female_1.work()  # Output: I can code

# 🔹 Accessing inherited attribute
print(f"Age of female_1: {female_1.age}")  # Output: 20

# 🚀 Creating an object of Male
male_1 = Male("Raj", 25, "Delhi")  # name = Raj, age = 25, location = Delhi

# 🔹 Calling inherited method from Human
male_1.eat()  # Output: I can eat

# 🔹 Calling Male-specific method
male_1.sleep()  # Output: I can sleep whole day

# 🔹 Accessing Male-specific attribute
print(f"Location of male_1: {male_1.location}")  # Output: Delhi

# 🔹 Showing full details using method from Human
male_1.showDetails()  # Output: Name: Raj, Age: 25
