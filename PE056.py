biggest = 0
for a in range(1, 100):
    for b in range(1, 100):
        s = sum([int(d) for d in str(a ** b)])
        if s > biggest:
            biggest = s
print(biggest)
