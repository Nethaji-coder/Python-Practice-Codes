tup1 = (10, 20, 40.5, 'Kodnest', 10)
print(tup1)#(10, 20, 40.5, 'Kodnest', 10)
#tup1.append(500)=Error
#tup1.remove(20)=Error
#tup1.pop()=Error
#del tup1[2]=Error
print(tup1[3])#Kodnest

#Deletes the complete tup1 object
del tup1
#print(tup1)#Error

#Concatination of tuples
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)#(1, 2, 3, 4, 5, 6)

#Create a Singleton tuple
tup = (10,)
print(tup,type(tup))#(10,) <class 'tuple'>

#Un packing of tuple
new_tup = (10,20,30,40)
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1:',ele1)#Value of ele1: 10  
print('Value of ele2:',ele2)#Value of ele2: 20  
print('Value of ele3:',ele3)#Value of ele3: 30  
print('Value of ele4:',ele4)#Value of ele4: 40  
