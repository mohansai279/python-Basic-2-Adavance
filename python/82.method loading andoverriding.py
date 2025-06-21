class Student:
    def introduce(self, name, age=None):  # default argument
        if age:
            print(f"My name is {name} and I am {age} years old.")
        else:
            print(f"My name is {name}.")
#method overload
s = Student()
s.introduce("Rahul")         # Output: My name is Rahul.
s.introduce("Rahul", 20)     # Output: My name is Rahul and I am 20 years old.
#method overriding

class CollegeStudent(Student):
    def introduce(self, name, age=None):
        if age:
            print(f"I’m {name}, {age} years old, and I’m a college student.")
        else:
            print(f"I’m {name} and I’m a college student.")
c = CollegeStudent()
c.introduce("Nisha")         # Output: I’m Nisha and I’m a college student.
c.introduce("Nisha", 19)     # Output: I’m Nisha, 19 years old, and I’m a college student.
