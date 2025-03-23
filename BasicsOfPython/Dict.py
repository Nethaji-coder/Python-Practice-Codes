d1 = {'name':'Priya','age':27,'phone':7670899807}
print(d1,type(d1))#{'name': 'Priya', 'age': 27, 'phone': 7670899807} <class 'dict'>

#In dict we cannot store duplicate keys.
d1['name']= 'Pooja'
print(d1)#{'name': 'Pooja', 'age': 27, 'phone': 7670899807}

#In dict we can store duplicate values.
marks = {'sci':85,'Maths':85} #Allowed

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)


