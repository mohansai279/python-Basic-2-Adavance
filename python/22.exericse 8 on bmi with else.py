weigth = int(input("enter weight in kgs:"))
height = float(input("enter weight in meter: "))
bmi=weigth/height**2
print(bmi)
print(round(bmi,2))
if(bmi<18.5):
    print(" you are in under weight")
elif(bmi<25):
    print("ypu are in normal weight")
elif(bmi<30):
    print("you are in under weight")
elif(bmi<35):
    print("you are obese")
elif (bmi<=40):
    print("gym ki ellu mayya")
else:
    print("pothavu na kodaka tharolani")