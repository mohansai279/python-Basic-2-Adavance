class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# One function that works for any animal!
def make_pet_speak(pet):
    pet.speak()

# Now press the same button for each pet!
make_pet_speak(Dog())   # Bark!
make_pet_speak(Cat())   # Meow!


# You have 3 pets at home:

# 🐶 A dog that says: "Bark!"

# 🐱 A cat that says: "Meow!"

# 🐮 A cow that says: "Moo!"

# Now you want to tell each pet to speak, but you don’t want to write special code for each one.

