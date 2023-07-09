def fibonacci(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    else:
        a = fibonacci(n-1) + fibonacci(n-2)
        return a
s = fibonacci(6)
print(s)