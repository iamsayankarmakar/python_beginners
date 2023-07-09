s = input()
l1 = list(s)
print(l1)
i = 0
a = 0
while i < len(l1):
    if l1[i].isalnum():
        a += 1
    i += 1

if a > 0:
    print("True")
else:
    print("False")

i = 0
a = 0
while i < len(l1):
    if l1[i].isalpha():
        a += 1
    i += 1
if a > 0:
    print("True")
else:
    print("False")


i = 0
a = 0
while i < len(l1):
    if l1[i].isdigit():
        a += 1
    i += 1

if a > 0:
    print("True")
else:
    print("False")


i = 0
a = 0
while i < len(l1):
    if l1[i].isupper():
        a += 1
    i += 1
if a > 0:
    print("True")
else:
    print("False")


i = 0
a = 0
while i < len(l1):
    if l1[i].islower():
        a += 1
    i += 1
if a > 0:
    print("True")
else:
    print("False")


