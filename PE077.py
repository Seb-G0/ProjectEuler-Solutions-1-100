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

primes = SieveOfEratosthenes(1000)
def PE077(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in primes:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]-1

n = 1
while PE077(n) < 5000:
    n += 1
print(n)