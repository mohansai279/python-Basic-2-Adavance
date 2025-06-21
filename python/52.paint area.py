import math 

def paint_calculation(height,width,cover):
    area=height*width
    number_of_cans=math.ceil(area/cover)
    print(f"you will need {number_of_cans} can of paint")
h=int(input("enter the height of the wall in metes:\n"))
w=int(input("enter the height of the wall in meters:\n"))
coverage=7
paint_calculation(width=w,height=h,cover=coverage)