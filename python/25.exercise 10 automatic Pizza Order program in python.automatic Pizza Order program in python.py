# Pizza size prices
small_price = 100
medium_price = 200
large_price = 300
extra_cheese_price = 20

# Get user choice
pizza_size = input("What size pizza do you want? (small/medium/large): ").lower()

# Initialize bill
bill = 0

# Set base price
if pizza_size == "small":
    bill = small_price
elif pizza_size == "medium":
    bill = medium_price
elif pizza_size == "large":
    bill = large_price
else:
    print("Invalid pizza size.")
    exit()

# Ask for peperoni
peperoni = input("Would you like to add peperoni (y/n)? ").lower()

if peperoni == "y":
    if pizza_size == "small":
        bill += 30
    else:  # medium or large
        bill += 50

# Ask for extra cheese
extra_cheese = input("Would you like extra cheese (y/n)? ").lower()
if extra_cheese == "y":
    bill += extra_cheese_price

# Final bill
print(f"The total bill is {bill}. Thank you for your order!")
