height = int(input("What is your height (in feet): "))

if height >= 3:
    print("You can ride.")
    
    age = int(input("What is your age: "))
    if age <= 12:
        bill = 150
        print("Ticket price is 150")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250")
    else:
        bill = 500
        print("Ticket price is 500")

    photo = input("Do you want to take a photo (y/n)? ")

    if photo.lower() == 'y':
        bill += 50
    elif photo.lower() == 'n':
        bill += 0
    else:
        print("Invalid input for photo. No extra charges applied.")

    print(f"The total bill amount is {bill}. Thank you, have a good ride!")

else:
    print("You can't ride.")
