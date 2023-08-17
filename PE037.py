from time import time
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
def istrunctable(n):
    left = n
    right = n
    i = 1
    while len(str(left)) != 1:
        left //= 10
        right = (n % (10**i))
        i += 1
        if not(isprime(left)) or not(isprime(right)):
            return False
    return True

#upper limit guess
primes = SieveOfEratosthenes(1000000)
results = []
index = 4 #ignore one digit primes

start = time()

while len(results) < 11:
    p = primes[index]
    if any(int(digit) % 2 == 0 and int(digit) != 2 for digit in str(p)):
        index += 1
        continue
    if istrunctable(p):
        results.append(p)
        index += 1
    else:
        index += 1
print(sum(results))