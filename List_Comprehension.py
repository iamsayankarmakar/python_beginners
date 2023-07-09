# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# l1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(l1)
l1 =[2, 3, 6, 6, 5]
max = l1[0]
for i in range(len(l1)):
    if l1[i] > max:
        max = l1[i]
        print(max)
    else:
        max =l1
