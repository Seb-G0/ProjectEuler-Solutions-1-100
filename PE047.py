def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def PE047():
    n = 1
    while True:
        if len(set(prime_factors(n))) == 4:
            if len(set(prime_factors(n + 1))) == 4:
                if len(set(prime_factors(n + 2))) == 4:
                    if len(set(prime_factors(n + 3))) == 4:
                        return n
        n += 1
print(PE047())
