li1 = [10,20,40.50,True,"Kodnest",20]
print(li1,type(li1))#[10, 20, 40.5, True, 'Kodnest', 20] <class 'list'>

#append(): Will add element at the end of the list,it will add only one element at a time
li1.append(300)
print(li1)#[10, 20, 40.5, True, 'Kodnest', 20, 300]    

#insert(index, element): Will add the given element at the given index value in the list
li1.insert(1,15)
print(li1)#[10, 15, 20, 40.5, True, 'Kodnest', 20, 300]

#remove(element):Will removes the first occrurrence of the element in the list
li1.remove(20)
print(li1)#[10, 15, 40.5, True, 'Kodnest', 20, 300] 

#in and not in Operator:
print(2000 in li1)#False
print('Kodnest' in li1)#True

#pop(): Without argument will delete and return last element from list
removed_element=li1.pop()
print(removed_element)#300
print(li1)#[10, 15, 40.5, True, 'Kodnest', 20]

#pop(index): With argument will delete and remove the element at specified index in the list
removed_ele=li1.pop(4)
print(removed_ele)#Kodnest
print(li1)#[10, 15, 40.5, True, 20]

#del: Is used to delete the elememt in the list at the given index value
#pop() is a bult in function which will return the deleted value, where as del is an keyword which will not return the deleted value
del li1[1]
print(li1)#[10, 40.5, True, 20]