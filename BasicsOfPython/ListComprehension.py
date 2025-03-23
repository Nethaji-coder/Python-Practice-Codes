li1 = [1,2,3,4,5]
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(sq_li)#[1, 4, 9, 16, 25]

#using listComprehension
#When we have only if part then write it after for loop
duplicate_li1 = [i for i in li1]
print(duplicate_li1)#[1, 2, 3, 4, 5]

even = [i for i in li1 if i%2 == 0]
print(even)#[2, 4]

sq_list = [i**2 for i in li1]
print(sq_list)#[1, 4, 9, 16, 25]

#if and else both in one list comprehension
#When we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'odd' for i in li1]
print(even_odd)#['odd', 'even', 'odd', 'even', 'odd']

#Multiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)#[10,20,30,40,50,60]