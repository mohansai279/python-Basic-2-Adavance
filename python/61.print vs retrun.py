def func1(a,b):
    c= a+b
    print(c)
output1=func1(3,4)
print(output1)

#########################
def func3(x):
    return x+1

def func2(a,b):
    c= a+b
    return c
output2=func2(3,4)
final_output=func3(output2)
print(final_output)

