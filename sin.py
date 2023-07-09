from math import sin, pi
actual = sin(pi/2)
c = pi/2
d = abs(c - actual)
term = pi/2
x = pi/2
n = 1
while d > 10**(-4):
    term *= -(x**2)/((2*n)*(2*n + 1))
    n += 1
    c += term
    d = abs(c - actual)

print(c)
print(n)
print(actual)
print(d)
