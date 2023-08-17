target = 1000000000000
def PE100(n):
    if n == 1:
        return 3
    if n == 0:
        return 1
    return 6 * PE100(n - 1) - PE100(n - 2) - 2
n = 1
while PE100(n) < target:
    n += 1
print(PE100(n-1))