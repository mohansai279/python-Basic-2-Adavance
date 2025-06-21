class Student:
    def __init__(self, name, rollno, age):
        self.name = name          # ✅ Public
        self._rollno = rollno     # ⚠️ Protected
        self.__age = age          # 🔒 Private

    def show(self):
        print(f"Name: {self.name}")         # Public
        print(f"Roll No: {self._rollno}")   # Protected
        print(f"Age: {self.__age}")         # Private (inside class)

# Create object
s1 = Student("Rahul", 23, 21)

# Access public
print(s1.name)           # ✅ Allowed

# Access protected
print(s1._rollno)        # ⚠️ Allowed (but not recommended)

# Access private directly (❌ will cause error)
# print(s1.__age)        # ❌ Error

# Access private using name mangling (⚠️ Not recommended)
print(s1._Student__age)  # ✅ Allowed, but should be avoided

# Call method to show all
s1.show()
