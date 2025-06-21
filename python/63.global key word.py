a=10
def display():
    
    print(a)
display()

a=10
def display():
    a=15
    print(a)
display()


# def display():
#     a=15
    
# display()           }--------> error occurs because accesing global from local
# print(a)

a=18
def display():
    global a
    print(a)
display()

