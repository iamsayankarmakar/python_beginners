d = "-"
p = ".|."
N, M = map(int, input().split())
w = "WELCOME"
for i in range(N):
    if int(N/2) == i:
        print(w.center(M, d))
    elif i < int(N/2):
        print((p * (2*i + 1)).center(M, d))
    else:
        print((p * (2 * (N - 1-i) + 1)).center(M, d))
