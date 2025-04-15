def disp():
    return 10
    return 20
    return 30

print(disp()) #10
print(disp()) #10
print(disp()) #10

def generator_function():
    yield 10
    yield 20
    yield 30

ref = generator_function()
print(next(ref))
print(next(ref))
print(next(ref))
#print(next(ref)) #StopIteration

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        print(a)
        a,b = b,a+b
fibonacci(10)

def fibonacci_gen(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = b,a+b

ref = fibonacci_gen(10)
print(next(ref)) #0
print(next(ref)) #1

#for i in range(5):
#   print(next(ref))