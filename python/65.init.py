class Instructor:
    def __init__(self, ins_name, address):
        print("Creating a new object")
        self.name = ins_name
        self.address = address
        self.followers=0
        
instructor_1=Instructor("mohan","vizag")
print(instructor_1.name)
print(instructor_1.followers)
instructor_2=Instructor("jenny","delhi")
print(instructor_2.name)
        
#or .bu these take more lines
# instructor_1=Instructor()
# instructor_1.name="mohan"
# instructor_1.address="delhi"
# print(instructor_1.name)
