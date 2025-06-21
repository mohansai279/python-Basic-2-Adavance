#What is Classic Diamond Shape Problem in Multiple Inheritance in Python
class A:
    def display(self):
        print("display from A class")
        
class B(A):
    
    def display(self):
        print("display From B class")
        
class c(A):

    def show(Self):
        print("hi from c class")
    def display(self):
        print("dipaly from c class")
        
class D(B,c):
    
    def display(self):
        print("dixplay from d class")
        
d1=D()
d1.display()
print(D.__mro__)

