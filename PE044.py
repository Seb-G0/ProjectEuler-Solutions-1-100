from math import sqrt, ceil
def PE044():
    a = 1
    while True:
        b = 1
        while b <= a:
            c = (sqrt(1 + 12 * (3 * (a ** 2 + b ** 2) - a - b)) + 1) / 6
            d = (sqrt(1 + 12 * (3 * (a ** 2 - b ** 2) - a + b)) + 1) / 6
            if c == ceil(c) and d == ceil(d):
                result = int((a * ((3 * a) - 1) / 2) - (b * ((3 * b) - 1) / 2))
                return result
            b += 1
        a += 1
print(PE044())