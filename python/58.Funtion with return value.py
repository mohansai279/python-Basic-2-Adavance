def add(a,b):
    c= a+b
    return c
    # print(c)
    # return c
add(4,4)
print(add(5,4))
result=add(3,4)
print(result)

def format_name(f_name,l_name):
    formateed_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formateed_f_name}{formatted_l_name}"
        
formatted_name=format_name("Mohan","Ampolu")
print(formatted_name)
     