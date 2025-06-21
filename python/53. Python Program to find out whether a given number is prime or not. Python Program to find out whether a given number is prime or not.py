# Python Program to find out whether a given number is prime or not.

# def primechecker(number):
#     is_prime=True
#     if number==1:
#         is_prime=False
#     for i in range (2,number):
#         if number%i==0:
#             is_prime=False
#     if is_prime==True:
#         print("it prime ")
#     else:
#         print("not a prime")
    
    
# n=int(input("enter an number:"))


# primechecker(n)

n=int(input("enter an number:"))
if n<=1:
    print("it is neither prime nor compiste number")
else:
    for i in range(2,n):
        if n%i==0:
            print("it is a compisite number")
            break
    else:
        print("it is prime a number")