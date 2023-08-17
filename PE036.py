total = 0
for num in range(1, 1000000):
    if num == int(str(num)[::-1]) and int(str(bin(num))[2:]) == int(str(bin(num))[2:][::-1]):
        total += num
print(total)