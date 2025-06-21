import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    #return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
    # end of the function 
print(mean_median_mode([3,5,45,3,2,1,89]))
a,b,c=mean_median_mode([3,5,45,3,2,1,89])
print(f"mean is {a} \n median is {b} \n mode is {c}")

def add(a,b):
    if a==0 & b==0:
        return 
    else:
        return a+b
var1=int(input("enter first variable:\n"))
Var2=int(input("enter the second variable:\n"))
result=add(var1,Var2)
print(result)


