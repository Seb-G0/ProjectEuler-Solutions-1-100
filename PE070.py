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

limit = 10 ** 7
primes = SieveOfEratosthenes(int(limit ** 0.5) + 500)
def totient(p1, p2):
    return (p1 - 1) * (p2 - 1)
min = 9
value = None
for p1 in primes:
    for p2 in primes[primes.index(p1) + 1: ]:
        if p1 * p2 > limit:
            continue
        num = p1 * p2
        v = totient(p1, p2)
        if sorted(str(num)) == sorted(str(v)):
            if num / v < min:
                min = num / v
                value = num
print(value)