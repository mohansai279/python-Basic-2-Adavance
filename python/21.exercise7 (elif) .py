a=52
if a%2==0:
    print("even")
    if(a>30):
        print("number is greater than 30..!")
print("bye")

height = int(input("what is your height "))
if height>=3:
    print("can ride")
    age=int(input("what is your age"))
    if age<=18:
        print("pleas pay 250 Rs:")
    elif age<=25:
        print("pleas pay 300 rs")
    else:
        print("please pay 500 rs:")
else:
    print("can't ride")
    
 