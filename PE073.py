from math import gcd
count = 0
i = 12000
for d in range(1, i + 1):
    for n in range(1,d):
        if gcd(n, d) == 1:
            if n/d > 1/3 and n/d < 1/2:
                count += 1
print(count)