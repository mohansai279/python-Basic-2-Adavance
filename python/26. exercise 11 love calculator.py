your_name= input("what is your name?")
partner_name=input("what is your partner_name?")
your_name=your_name.lower() 
partner_name=partner_name.lower()
combine_string=your_name + partner_name
print(combine_string)
print(f"The both couple name are {your_name} and {partner_name}")
t= combine_string.count('t')
r= combine_string.count('r')
u= combine_string.count('u')
e= combine_string.count('e')

true=t+r+u+e

l= combine_string.count('l')
o= combine_string.count('o')
v= combine_string.count('v')
e= combine_string.count('e')
love= l+o+v+e

love_score=int(str(true) +str(love))

if love_score<10 or love_score>90:
    print(f" your love socre is {love_score} and you go together")
elif love_score>=40 and love_score<=50:
    print(f" you love score is {love_score}")
else:
    print(f"your love score is {love_score}")
