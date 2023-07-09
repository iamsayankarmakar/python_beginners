if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l1 =list(arr)
    print(l1)
    l1.sort()
    print(l1)
    m = max(l1)
    while m == max(l1):
        l1.remove(max(l1))
    print(l1)
    print(max(l1))
