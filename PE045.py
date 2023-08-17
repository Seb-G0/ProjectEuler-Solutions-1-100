from math import sqrt
def getHex(n):
    return n * (2 * n - 1)
def isPenta(n):
    return ((1 + sqrt(24 * n + 1)) / 6).is_integer()
def PE045():
    n = 144
    while True:
        val = getHex(n)
        if isPenta(val):
            return val
        n += 1
print(PE045())