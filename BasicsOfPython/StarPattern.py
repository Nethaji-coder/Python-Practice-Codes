#For square
rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        print('*',end=' ')
    print()

print()

# For increasing triangle
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()

print()

# For decreasing triangle
for i in range(rows):
    for j in range(i,rows):
        print('*',end=' ')
    print()

print()

# For right pascal triangle
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*',end=' ')
    print()

print()

# For Butterfly Pattern
for i in range(rows):
    for j in range(i+1):
        print('*',end=" ")
    for j in range(i,rows-1):
        print(' ',end=" ")
    for j in range(i,rows-1):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*',end=" ")
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i, rows-1):
        print('*',end=" ")
    print()

print()

# For Diamond Pattern
for i in range(rows-1):
    for j in range(i,rows):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    for j in range(i):
        print('*',end=" ")
    print()
for i in range(rows):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,rows):
        print('*',end=" ")
    for j in range(i,rows-1):
        print('*',end=" ")
    print()