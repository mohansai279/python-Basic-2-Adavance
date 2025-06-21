#Python Program to find out Area and Circumference of a Circle using Class and Objects(OOP concepts)
class Circle:
    pi=3.14 #class object attribute
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def circumference(self):
        return 2*self.pi*self.radius
circle_1=Circle(4)
print(circle_1.circumference())
circle_2=Circle(14)
print(circle_2.circumference())
print(circle_1.area)