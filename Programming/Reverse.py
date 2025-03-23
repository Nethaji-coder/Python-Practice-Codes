#object.reverse(): Will reverse the original object
li = [10,20,30,40,50]
print('Before Reverse:',li)#Before Reverse: [10, 20, 30, 40, 50]
li.reverse()
print('After Reverse:',li)#After Reverse: [50, 40, 30, 20, 10]

#list(reversed(iterable_object)):
li2 = [11,27,69,55]
reverse_li2 = list(reversed(li2))
print(li2)#[11, 27, 69, 55]
print(reverse_li2)#[55, 69, 27, 11]

li3 = [1,2,3,4,5]
new_reverse_li3 = list(reversed(li3))#--> Creating new reverse list
li3.reverse()#--> Reversing original list
print(new_reverse_li3)#[5, 4, 3, 2, 1]
print(li3)#[5, 4, 3, 2, 1]