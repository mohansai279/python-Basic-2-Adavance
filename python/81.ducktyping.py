#Uses a common parent class or interface
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Bark!
make_sound(Cat())  # Meow!
#duck typing start here
#“I don’t care who you are. If you quack, you’re a duck to me!”
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack like a duck!")

def make_it_quack(thing):
    thing.quack()

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I can quack like a duck!

