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

primes = SieveOfEratosthenes(1000000)
limit = 1000000
maxtotal = 0
maxrun = 0
for i in range(len(primes)):
    total = 0
    for j in range(i, len(primes)):
        total += primes[j]
        if total > limit:
            break
        if isprime(total) and total > maxtotal and j - i > maxrun:
            maxrun = j - i
            maxtotal = total
print(maxtotal)
