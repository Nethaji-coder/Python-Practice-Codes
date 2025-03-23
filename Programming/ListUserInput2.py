'''li = input('Enter space sperated elements')
print(li, type(li))#10 20 30 40 50 <class 'str'>
li = li.split()
print(li)#['10', '20', '30', '40', '50']
li = list(map(int,li))
print(li)#[10, 20]
'''
'''tup = tuple(map(int,input('Enter space separated elements').split()))
print(tup)#(10, 20)'''

li = list(map(int,input().split()))
print([i for i in li if i%2 == 0])#[10, 12]