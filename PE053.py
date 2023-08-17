def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def sequence(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))
count = 0
for n in range(1, 101):
    for r in range(1,n):
        if sequence(n,r) > 1000000:
            count += 1
print(count)