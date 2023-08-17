total = 0
for i in range(10,354294):
    if sum([int(j)**5 for j in str(i)]) == i:
        total += i
print(total)