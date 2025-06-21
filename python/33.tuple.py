tuple1=(2,3,6,8,5,3,4)
tuple2=(12,6,-8,"jeeny")
print(tuple1[1])
print(tuple2[3])
tuple4=(10,)
tuple5=(10)
print(type(tuple4))
print(type(tuple5))

#you caanot add or temove in tuple
print(tuple1[::2])
print(len(tuple1))
tuple6=(tuple1,tuple2,tuple4)#nesting of tuple
print(tuple6)
print(min(tuple6))
print(tuple1.count(3))
print(tuple1.index(3))
tuple7=(10,)*5
print(tuple7)

