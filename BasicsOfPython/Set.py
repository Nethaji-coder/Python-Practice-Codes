s1 = {10, True, "Kodnest", 10, 30, 44.5}
print(s1,type(s1))#{True, 'Kodnest', 10, 44.5, 30} <class 'set'>
#print(s1[0]):Error

#add(): used to add an element in the set.
s1.add(500)
print(s1)#{True, 'Kodnest', 500, 10, 44.5, 30}

s1.remove(44.5)
print(s1)#{True, 500, 'Kodnest', 10, 30}      

#pop(): Without index will delete and return one element
poped_ele = s1.pop()
print(poped_ele)#True
print(s1)#{500, 10, 'Kodnest', 30}