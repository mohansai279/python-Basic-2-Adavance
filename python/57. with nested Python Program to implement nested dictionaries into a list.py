student_data=[
    {
        "Name":"ram",
        "roll_no":10,
        "age":20,
        "course":"python"
    },
    {
        "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"java",
    }
    
]
# add new entre(name :shayam ,roll 22 ,age,18,course:c++)
def add_new_student(name,rollno,age,course):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course
    student_data.append(new_student)
add_new_student("shyam",22,18,"C++")
print(student_data)
