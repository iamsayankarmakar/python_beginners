from itertools import combinations
# s, k = input().split()
# s = sorted(s)
# k = int(k)
# #for i in range(1,k+1):
# for j in list(combinations(s, k)):
#     print("".join(j))
A = ['a',"a","c","d"]
combination_index = list(combinations(A, 2))
print(combination_index)