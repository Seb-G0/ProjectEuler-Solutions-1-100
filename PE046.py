from math import isqrt
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    if isprime(n):
        return False
    i = 1
    while i * i < n:
        if isprime(n - 2 * i * i):
            return False
        i += 1
    return True

def PE046():
    n = 3
    while True:
        if check(n):
            return n
        n += 2

print(PE046())