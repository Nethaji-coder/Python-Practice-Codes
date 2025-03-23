'''
syntax: for control_variable in iterable_object
'''
for i in 'Kodnest':
    print(i,end=" ")
print()

for j in [10,20,30]:
    print(j+5,end=" ")
print

for num in range(1,11):
    print(num,end=" ")
print()

for num in range(11,21,2):
    print(num, end=" ")
print()

for i in range(5):
    print(i,end=" ")
print()

#WAP to print all even numbers from 1-10.
for i in range(1,11):
    if(i%2==0):
        print(i, end=" ")
print()

i = 0
while(i<10):
    print(i+100,end=" ")
    i = i+1
print()

#WAP to print numbers from 1-10 if number is 6 then skip printing.
for i in range(1,11):
    if(i==6):
        continue
    print(i,end=" ")
print()

#WAP to print numbers from 1-10 but if number is 5 then stop printing.
for i in range(1,11):
    if(i==5):
        break
    print(i,end=" ")
print()

