set1={10,56,89,90,"jenny",10,1}
set2=set()
#set1[2]=99 gives you error because you cannot add in middle of the set
print(type(set1))
print(type(set2))
print(len(set1))
set1.add(99)
print(set1)
set1.add(90)
print(set1)
set1.discard(10)
print(set1)
print(set1.pop())
print(set1)
