# Keeping money safe
row1=[1,1,1] 
row2=[1,1,1]
row3=[1,1,1]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
postion=input("enter the postion where you want to hide the money")
#32
row_number=int(postion[0])
colunm_number=int(postion[1])
row_selected=matrix[row_number-1]
row_selected[colunm_number-1]='x'
print(f"{row1}\n{row2}\n{row3}")
