# 👤 Base class
class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat.")

# 👨 Derived class 1 (inherits from Human)
class Male(Human):
    def walk(self):
        print(f"{self.name} can walk like a man.")

# 👩 Derived class 2 (inherits from Human)
class Female(Human):
    def talk(self):
        print(f"{self.name} can talk like a woman.")

# 🧑‍💼 Hybrid class (inherits from both Male and Female)
class Employee(Male, Female):  # Multiple inheritance
    def work(self):
        print(f"{self.name} can work as an employee.")

# 🚀 Create object of Employee class
emp1 = Employee("Alex")

# 🔹 Access methods from all parent classes
emp1.eat()     # From Human
emp1.walk()    # From Male
emp1.talk()    # From Female
emp1.work()    # From Employee
