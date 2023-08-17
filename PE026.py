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

def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

def findreptendlength(n):
    a = 10
    if (GCD(a, n) != 1):
        return -1
    result = 1
    i = 1
    while (i < n):
        result = (result * a) % n
        if (result == 1):
            return i
        i = i + 1
    return -1

primes = SieveOfEratosthenes(1000)
primes.reverse()
max = [0, 0]
for i in primes:
    if i == 2 or i == 5:
        continue
    else:
        value = findreptendlength(i)
        if value > max[0]: max[0], max[1] = value, i
print(max[1], "has the longest cycle of", max[0])