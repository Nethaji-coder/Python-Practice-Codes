def swapcase(s):
    sample = ''
    for i in s:
        if i.islower():
            sample += i.upper()
        else:
            sample += i.lower()
    return sample

s = input()
result = swapcase(s)
print(result)