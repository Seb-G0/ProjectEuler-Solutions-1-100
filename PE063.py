count = 0
for num in range(1,10):
    power = 1
    while power == len(str(num ** power)):
        count += 1
        power += 1
print(count)