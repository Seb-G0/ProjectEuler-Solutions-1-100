result = 0
def pythagoreanTriplets(lim):
    result = 0
    c, m = 0, 2
    while c < lim:
        for n in range(1,m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > lim:
                break
            if abs(2 * a - c) == 1:
                result += 2 * a + 2 * c
            if abs(2 * b - c) == 1:
                result += 2 * b + 2 * c
        m = m + 1
    return result
print(pythagoreanTriplets(1000000000//3 + 2))