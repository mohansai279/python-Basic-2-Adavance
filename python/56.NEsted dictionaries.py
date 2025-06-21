student_data={
    "Rama":{
        "roll_number":10,
        "age":20,
        "course":"python"
        },
    "Mohan":{"roll_number":10,"age":20,"course":"python"}

}
print(student_data["Mohan"])
print(student_data["Rama"])
print(student_data["Mohan"]["roll_number"])
del student_data["Mohan"]["roll_number"]
print(student_data["Mohan"])
#dictionrie wtih in list 
travel_data={
    "Gujarat":["dwarakadhish","somnath","state of unity"],
    "rajasthan":["jaipur","udaipur"]
}
print(travel_data["rajasthan"])
#list with in dictionarie - gives error 
