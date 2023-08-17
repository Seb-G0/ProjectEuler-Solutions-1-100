total = 0
for num in range(1,1000):
    total += num**num
print(total % 10 ** 10)