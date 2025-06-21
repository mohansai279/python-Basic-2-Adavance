heights=input("enter the heights weparated by space")
heights_split=heights.split()
count=0
for height in heights_split:
    count=count+1
print(count)
for i in range(count):
    heights_split[i]=int(heights_split[i])

total=0   
for person in heights_split:
    total+=person
print(total)
avg=total/count
print(round(avg))
    



