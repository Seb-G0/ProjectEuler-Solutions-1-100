from math import isqrt
def divisors(n):
    res = [1]
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res.append(i)
            if n/i != i:
                res.append(n//i)
    return sum(res)

results = []
abundantnums = set(n for n in range(12, 28124) if divisors(n) > n)
total = 0
for i in range(1, 28124):
    if any(i - a in abundantnums for a in abundantnums):
        continue
    total += i
print(total)