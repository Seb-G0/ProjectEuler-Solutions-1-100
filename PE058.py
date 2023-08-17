def isprime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return 0
    return 1

def getCorners(n):
    return n*n, n * n - n + 1, n * n - 2 * n + 2, n*n-3*n+3

def PE058():
    n = 3
    primes = 0
    total = 1
    ratio = 1
    while ratio > 0.1:
        primes += sum([isprime(i) for i in getCorners(n)])
        total += 4
        ratio = primes / total
        n += 2
    return n - 2
print(PE058())