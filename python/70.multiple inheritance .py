class Human:
    
    def eat(self):
        print("I can eat")
    def work(self):
        print(" i can work")

class Male:
    
    def flirt(self):
        print("I can flirt")
    def work(self):
        print(" i can code")


class boy(Human,Male):
    def sleep(self):
        print(" i can sleep ")
    def work(self):
        print(" i can test")
            


boy_1 = boy()
boy_1.flirt()
boy_1.work()
print(boy.mro())
# Male.work(boy_1)