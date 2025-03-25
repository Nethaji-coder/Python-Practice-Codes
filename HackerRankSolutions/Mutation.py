def mutation(s, position, char):
    li = list(s)
    li[position] = char
    res = ''.join(li)
    return res
s = input()
p, c = input().split()
s_new = mutation(s, int(p), c)
print(s_new)