class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart

        
    def eat(self):
        print("I can eat")
    def worK(self):
        print("I can work")

class Male(Human):
    def __init__(self, name,heart):
        super().__init__(heart)
        self.name=name

    def flirt(self):
        print("I can flirt")
    def worK(self):
        super().worK() # i takes from main or parent class
        print("I can code")  # Overriding
    def display(self):
         print(f" human I am {self.name} and i have { self.num_heart} heart and {self.num_eyes}")
         

male_1 = Male("Mohan sai",1)
male_1.eat()
male_1.flirt()
male_1.worK()
print(male_1.name)
print(male_1.num_eyes)
print(male_1.num_heart)