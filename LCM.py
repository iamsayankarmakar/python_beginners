def lcm(a, b):
    if b > a and b % a == 0:
        return b
    elif a > b and a % b == 0:
        return a
    elif a % b != 0 and b > a:
        num_b = b
        while True:
            num_b += 1
            if num_b % a == 0 and num_b % b == 0:
                return num_b
                break
    else:
        num_a = a
        while True:
            num_a += 1
            if num_a % a == 0 and num_a % b == 0:
                return num_a
                break


print(lcm(3, 2))
print(lcm(10,12))