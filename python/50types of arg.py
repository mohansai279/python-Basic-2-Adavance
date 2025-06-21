#default
def greet(name ,dept):
    print(f"hi{name}")
    print(f" are you from {dept} depat")
greet("mohan","cs")
#key word
def greet(name ,dept):
    print(f"hi{name}")
    print(f" are you from {dept} depat")
greet(dept="cs",name="mohan")
#positional with keyword
def greet(name ,dept):
    print(f"hi{name}")
    print(f" are you from {dept} depat")
# greet(dept="cs","mohan") # it shows error boecause postional will not follow key word
greet("mohan",dept="cs")
#overridiing the values
def greet(name ,dept="cs",subject="c.s.e"):#default arg must be publish after the naming of the non default arguments
    print(f"hi{name}")
    print(f" are you from {dept} depat")
    print(f"what is the subject you teach{subject}")
    

greet("mohan",dept="MEC")

#aribritary argumnents(*numbers) 
def add(*numbers):#(a,b,c) tuple
    c=0
    for i in numbers:
        c=c+i
        print(f"sum is {c}")
    add(5,7,9)
    
    
    
