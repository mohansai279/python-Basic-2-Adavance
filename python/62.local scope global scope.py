a=10#globl
def display():
    a=15#local
    print(a)
display()
print(a)

a=10#globl
def display():
    global a
    a=15#local
    print(a)
display()
print(a)

a,b=5,6

if a<b:
    c=a+b
print(c)
