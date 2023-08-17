from math import gcd, sqrt
limit = 1500000
mlimit = int(sqrt(limit/2))
d = dict()
for m in range(2, mlimit):
    for n in range(1, m):
        if (((n + m) % 2) == 1 and gcd(n, m) == 1):
            a = m * m + n * n
            b = m * m - n * n
            c = 2 * m * n
            p = a + b + c
            while p <= limit:
                if p in d.keys():
                    d[p] += 1
                else:
                    d[p] = 1
                p += a + b + c
print(sum([i if i == 1 else 0 for i in d.values()]))
