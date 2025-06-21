# def add(*numbers): #*args (1,2)---. tuple
#     for i in numbers:
#         c=0
#         print(numbers[0])
    
#         for i in numbers:
#             c=c+i
#         print(f"sum is {c}")
            
    
    
# add(1,2)
# add(6,4,2)
# add(4,5,6,7,89)

# def add(*numbers,name): #*args (1,2)---. tuple # --> gives eeror  because not mentioned as key word 
#     for i in numbers:
#         c=0
#         print(numbers[0])
    
#         for i in numbers:
#             c=c+i
#         print(f"sum is {c}")
            
    
    
# add(1,2)
# add(6,4,2)
# add(4,5,6,7,89)

# def add(*numbers,name): #*args (1,2)---. tuple
#     for i in numbers:
#         c=0
#         print(numbers[0])
#         print(name)
     
#         for i in numbers:
#             c=c+i
#         print(f"sum is {c}")
            
    
    
# add(1,2,3,name="mohan")
# add(6,4,2)
# add(4,5,6,7,89)

#-------------------------------------------------------------------
#arbitary keyword argument
#---------------------------------------------------------------------
def info_Person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        
    
info_Person(name="ram",age="30",dept="cse")
info_Person(name="sham",dept="cse")

# def info_Person(**kwargs,*args):# not posiible gives error 
#     for key,value in kwargs.items():
#         print(key,value)
        
    
# info_Person(name="ram",age="30",dept="cse")
# info_Person(name="sham",dept="cse")

def info_Person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
    
info_Person(1,2,name="ram",age="30",dept="cse")
info_Person(1,2,3,name="sham",dept="cse")

