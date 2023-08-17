def isprime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


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


primes = SieveOfEratosthenes(10000) #Estimated Max


def PE060():
    for p1 in primes:
        for p2 in primes[primes.index(p1) + 1:]:
            if isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1))):
                for p3 in primes[primes.index(p2) + 1:]:
                    if isprime(int(str(p1) + str(p3))) and isprime(int(str(p3) + str(p1))) and isprime(int(str(p2) + str(p3))) and isprime(int(str(p3) + str(p2))):
                        for p4 in primes[primes.index(p3) + 1:]:
                            if isprime(int(str(p1) + str(p4))) and isprime(int(str(p1) + str(p4))) and isprime(int(str(p4) + str(p2))) and isprime(int(str(p2) + str(p4))) and isprime(int(str(p3) + str(p4))) and isprime(int(str(p4) + str(p3))):
                                for p5 in primes[primes.index(p4) + 1:]:
                                    if isprime(int(str(p1) + str(p5))) and isprime(int(str(p5) + str(p1))) and isprime(int(str(p5) + str(p2))) and isprime(int(str(p2) + str(p5))) and isprime(int(str(p3) + str(p5))) and isprime(int(str(p5) + str(p3))) and isprime(int(str(p5) + str(p4))) and isprime(int(str(p4) + str(p5))):
                                        return p1 + p2 + p3 + p4 + p5


print(PE060())
