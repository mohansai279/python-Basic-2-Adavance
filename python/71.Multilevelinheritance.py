class Human:
    can_breath = True

    def __init__(self, num_heart):
        print("Calling init from Human class")
        self.eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")


class Male(Human):
    def __init__(self, name):
        print("Calling init from Male class")
        self.name = name

    def sleep(self):
        print("I can sleep the whole day")


class Boy(Male):
    def __init__(self, name, num_heart, can_dance):
        Human.__init__(self, num_heart)
        Male.__init__(self, name)
        self.know_dancing = can_dance

    def work(self):
        super().work()  # Calls the work() method from Human
        print("I can work hard")


# Creating a Boy object with correct parameters
boy_1 = Boy("John", 1, True)

# Calling methods
boy_1.eat()
boy_1.sleep()
boy_1.work()
