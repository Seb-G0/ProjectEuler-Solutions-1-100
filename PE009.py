def triplet(m, n):
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return a, b, c

def PE009():
    m = 1
    while True:
        n = 1
        while n < m:
            a, b, c = triplet(m, n)
            if a + b + c == 1000:
                return a * b * c
            n += 1
        m += 1
print(PE009())

