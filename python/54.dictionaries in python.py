# phone_no={
#     'ram':12345,
#     'Mohan':98765,
#     'jenny':1432
    
# } 1 type of represntation

phone_no={ 'ram':12345, 'Mohan':98765,'jenny':1432}  # 2 type of represntation
# print(phone_no['shayam']) error it shows #Mohan=9865 is not write way to represnt 

print(phone_no['ram'])

phone_no=dict({ 'ram':12345, 'Mohan':98765,'jenny':1432})# 3 rd type of represntation
print(phone_no)
phone_no['Mohan']=879027 #updating
print(phone_no)
#nested dictianrie
phone_no['Mohan']={879027,733081,9493}
print(phone_no)
phone_no['jenny']={'jeeny_office':908866,'jenny_personal':65432}
print(phone_no)
print(phone_no.get('Ram'))#nonne becuuase it is captital letter
print(phone_no.get('ram'))

data={
     1:'jeeny',
     0:'mohan',
     2:'karthik'
}
print(data[0])
del data[1]
print(data)
phone_no.pop('ram')
print(phone_no)
print((phone_no.values()))
print((phone_no.items()))
phone_no2=phone_no.copy()
print(phone_no2)
print(len(phone_no))

# print(phone_no.clear())




















