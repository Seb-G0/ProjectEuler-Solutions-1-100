def NumberofDevisors(n):
    count = 0
    for i in range(1, (int)(n ** 0.5) + 1):
        if (n % i == 0):
            if (n / i == i):
                count = count + 1
            else:
                count = count + 2
    return count

def PE012():
    n = 1
    while True:
        trinum = n * (n+1) / 2
        if NumberofDevisors(trinum) > 500:
            return int(trinum)
        n += 1

print(PE012())