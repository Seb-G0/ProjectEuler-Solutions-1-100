from functools import cache

@cache
def PE092(n):
    if n == 1:
        return 0
    if n == 89:
        return 1
    return PE092(sum(int(i) * int(i) for i in str(n)))

print(sum(PE092(n) for n in range(2, 10000000)))
