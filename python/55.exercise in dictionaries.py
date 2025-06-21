#Python Program to assign grade to students based on their marks using Dictionaries.
student_marks={
    "mohan":90,
    "jenny":78,
    "dimpy":56,
    "rahul":41,
    "aniket":99,
    "prem":34
}
student_grades={}
for student in student_marks: # for key in some_dict:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    elif marks>50:
        student_grades[student]="c"
    elif marks>40:
        student_grades[student]="D"
    else:
        student_grades[student]="F"
print(student_grades)       