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

primes = SieveOfEratosthenes(20)
total = 1
n = 0
while total < 1000000:
    total *= primes[n]
    n += 1
print(total // primes[n-1])
#totient is minimized when value has the most prime factors.

