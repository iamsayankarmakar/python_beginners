from itertools import groupby
x = "aaaabbbccd"
new =groupby(x)
print(new)
new_1 = [list(g) for k, g in new]

print(new_1)
