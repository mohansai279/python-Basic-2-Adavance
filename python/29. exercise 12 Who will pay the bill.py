import random

name=input("enter the names of ypur friends")
name_split=name.split(" ")
print(name_split)
length=len(name_split)
random_choice = random.randint(0,length-1)
print(f"{random_choice} will pay the bill")

