#Strings are immutable:
#1.Once we declare the string we cannot modifiy it, if we try to modifiy it new String object will be created .
#2.If the new string doesnot have any reference variable then it will be removed.
#3.Python Internally uses String Interning.
#4.String Interning is the process of checking string intern pool before creating any new object.
#5.When ever we want to create new object, python first will check string inter poll whether that object already exist or not.
#6.When object already exist int he string intern records then address of existing object will be reused.

#s1 = 'kodnest'
#s2 = s1.upper()
#print(s1)
#print(s2)

#s1 = 'K'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print('Id of H in s1: ',id(s1[0]))
print('Id of W in s2: ',id(s2[0]))

print('Id of O in s1: ',id(s1[-1]))
print('Id of O in s2: ',id(s2[1]))

print('Id of l in s1: ',id(s1[2]))
print('Id of l in s1: ',id(s1[3]))
print('Id of l in s2: ',id(s2[3]))