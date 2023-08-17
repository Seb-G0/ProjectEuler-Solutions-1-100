target = 2000000
error = 2000000
for x in range(1, 2001):
    for y in range(1, x):
        combinations = x * (x+1) * y * (y+1)/4
        if error > abs(combinations - 2000000):
            error = abs(combinations - 2000000)
            closest = x * y
print(closest)
