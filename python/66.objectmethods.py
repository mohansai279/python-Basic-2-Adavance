class Instructor:
    followers=0
    def __init__(self,name,address):
     self.name=name
     self.address=address
    def display(self,subject_name):
        print(f"hi, I am {self.name} and i teach {subject_name}")
    def update_followers(self,follower_name):
        self.followers+=1 
         
instructor_1=Instructor("mohan","vizag")
print(instructor_1.name)
instructor_1.display("python")
instructor_1.update_followers("")
print(instructor_1.followers)

#❌ So, if you create instructor_2 and call instructor_2.
# update_followers(), the count won’t become 2 — 
# each instance is modifying its own copy of the
# attribute, not the shared class variable. 

class Instructor:
    followers = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def update_followers(self, follower_name):
        Instructor.followers += 1

# Create two instructors
instructor_1 = Instructor("mohan", "vizag")
instructor_2 = Instructor("sita", "delhi")

# Update followers through both
instructor_1.update_followers("personA")
instructor_2.update_followers("personB")

# Output shared class attribute
print(Instructor.followers)  # ✅ Outputs: 2
