def PE003(n):
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
        d += 1
        if d*d > n:
            break
    return int(n)
print(PE003(600851475143))