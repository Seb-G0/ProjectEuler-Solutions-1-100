from math import isqrt
def divisors(n):
    res = [1]
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res.append(i)
            if n/i != i:
                res.append(n//i)
    return res

results = set()
for i in range(2,10000):
    n = sum(divisors(i))
    if i == sum(divisors(n)) and i != n:
        results.add(i)
        results.add(n)
print(sum(results))