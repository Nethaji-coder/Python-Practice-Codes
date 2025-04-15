li = [1,2,3,4,5]

def double(num):
    return num * 2
double_li = list(map(double,li))
print(double_li) #[2, 4, 6, 8, 10]

#filter(function, iterable_object)
def check_even(num):
    return num % 2 == 0
even_li = list(filter(check_even,li))
print(even_li) #[2, 4]

from functools import reduce
def mul(a,b):
    return a * b

res = reduce(mul,li)
print('Multiplication result is:',res)