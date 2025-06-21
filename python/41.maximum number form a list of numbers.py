# # with out for loop
# number=input("enter the list of numbers:")
# number_split=number.split()
# print(number_split)
# int_numbers=list(map(int,number.split()))
# #map(int, ...)
# # Purpose: Applies the int() function to each element in the list returned by .split().
# # What it does: Converts each string number to an integer.
# # List(...)
# # Purpose: Converts the map object into an actual list of integers.

# print(int_numbers)
# max_number=max(int_numbers)
# print(max_number)

number=input("enter the list of numbers:")
number_split=number.split()
print(number_split)
count=0

for number in number_split:
    count=count+1
print(f" the length of the list is: {count}")

for i in range(count):
    number_split[i]==int(number_split[i])

    
maximum_number = number_split[0]
for number in number_split:
    if number>maximum_number:
        maximum_number=number
        print(maximum_number)



