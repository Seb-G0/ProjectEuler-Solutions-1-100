n = [1,2]
m = [2 * i // 3 if i % 3 == 0 else 1 for i in range(1, 103)]
for i in range(99):
    n.append(m[i+1] * n[-1] + n[-2])
print(sum(int(i) for i in str(n[-1])))