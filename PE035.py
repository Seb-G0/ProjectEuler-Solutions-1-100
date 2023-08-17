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

primes = SieveOfEratosthenes(1000000)
count = 0
for p in primes:
    if p == 2 or p == 5:
        pass
    elif any(int(digit) % 2 == 0 or int(digit) == 5for digit in str(p)):
        continue
    for i in range(len(str(p))):
        rotate = int(str(p)[i:] + str(p)[:i])
        if rotate not in primes:
            break
    if rotate in primes:
        count += 1
print(count)
