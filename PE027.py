from math import isqrt

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

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

primes = SieveOfEratosthenes(1000)
count = 0
final_a = 0
final_b = 0
for a in range(-1000, 1000):
    for b in primes:
        p = 0
        while isprime(p * p + a * p + b):
            p += 1
        if count < p:
            count = p
            final_a = a
            final_b = b
print(final_b * final_a)