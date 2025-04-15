from functools import reduce
li = [1,2,3,4,5]

newli = list(filter(lambda num:num%2 == 0,li))
print(li)

sum = reduce(lambda a,b:a+b,li)
print(sum)

square = list(map(lambda num: num**2,li))
print(square)