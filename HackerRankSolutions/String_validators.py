'''#isalnum(): is used to check string contains alphabets or numbers
print('Kodnest123'.isalnum()) #True
print('Kodnest123#'.isalnum()) #False

#isalpha(): is used to check string contains only alphabets
print('Kodnest'.isalpha()) #True
print('Kodnest123'.isalpha()) #False

#isdigit(): is used to check striing contains only numbers
print('123'.isdigit()) #True
print('Kodnest123'.isdigit()) #False

#
print('apple'.islower()) #True
print('apple'.isupper()) #False

print(any([True,False,False])) #True
print(any((False,False,False))) #False'''

s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))