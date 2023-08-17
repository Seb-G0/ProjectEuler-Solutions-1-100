from math import isqrt
from collections import Counter
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
    n = int(n)
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

primes = SieveOfEratosthenes(1000000)
ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def PE051():
    for p in primes:
        if p % 100000 == p:
            continue
        if any(str(p).count(n) == 3 for n in ints):
            count = set()
            for n in ints:
                newprime = str(p).replace(Counter(str(p)).most_common(1)[0][0], n)
                if isprime(newprime) and str(int(newprime)) == str(newprime):
                    count.add(newprime)
            if len(count) >= 8:
                return min(count)
print(PE051())