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

primes = SieveOfEratosthenes(10 ** 7)
primes.reverse()
def isPandigital(p):
    if any(int(digit) > len(p) for digit in p):
        return False
    return len(set(p)) == len(p)

for p in primes:
    if isPandigital(str(p)):
        print(p)
        break
