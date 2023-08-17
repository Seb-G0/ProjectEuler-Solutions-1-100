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

primes = SieveOfEratosthenes(10000)

def PE049():
    for p in primes:
        if p % 1000 == p or p == 1487:
            continue
        count = [p]
        for j in primes[primes.index(p) + 1: ]:
            if sorted(str(p)) == sorted(str(j)):
                count.append(j)
        if len(count) == 3:
            if count[1] - count[0] == count[2] - count[1]:
                return str(count[0]) + str(count[1]) + str(count[2])
print(PE049())
