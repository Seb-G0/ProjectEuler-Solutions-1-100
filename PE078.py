from functools import cache

@cache
def p(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    total = 0
    for k in range(1, n + 1):
        total += (-1) ** (k+1) * (p(n - k * (3 * k - 1) // 2) + p(n - k * (3 * k + 1) // 2))
        if n-k*(3*k-1)//2 < 1:
            break
    return total
n = 1
while p(n) % 1000000 != 0:
    n += 1
print(n)