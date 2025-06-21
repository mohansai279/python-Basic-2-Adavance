number=[10,0,-1,7,8,9,1,23,5]
names=['jenny','krishna',"ram"]
mix_list=[1,'lenny',True]
print(number)
print(names)
print(mix_list)
print(number[-1])#negative indexing
print(number[0:4])#slicing
print(number[:4])#upt0 4
print(number[0:5:2])
number.sort()
print(number)
number.reverse()
print(number)
number.append(45)
print(number)
number.insert(2,45)
print(number)
number.extend(45)
print(number)
number[1:4]=[45,46,47]
print(number)
number.remove(0)
print(number)
