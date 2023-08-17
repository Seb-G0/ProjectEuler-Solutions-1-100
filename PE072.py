def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if n > 1:
        result -= result // n

    return int(result)

i = 1000000
count = 0
for d in range(2, i + 1):
    count += phi(d)
print(count)