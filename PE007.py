from math import log, floor
def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)
    return primes

def PE007(n):
    limit = floor(n * log(n * log(n)))
    return SieveOfEratosthenes(limit)[10000]
print(PE007(10001))
