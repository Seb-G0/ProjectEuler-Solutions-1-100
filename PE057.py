num = 3
den = 2
count = 0
for i in range(1001):
    if len(str(num)) > len(str(den)):
        count += 1
    num, den = (num + 2 * den), (num + den)
print(count)