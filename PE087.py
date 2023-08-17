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

primes = SieveOfEratosthenes(7071)
s = set()
for a in primes:
    for b in primes:
        if b**3 > 50000000: break
        for c in primes:
            if c**4 > 50000000: break
            v = a**2 + b**3 + c**4
            if v > 50000000: break
            else: s.add(v)
print(len(s))