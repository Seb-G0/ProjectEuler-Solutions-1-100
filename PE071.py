lim = 1000000
closest = [1, lim]
for d in range(1, lim + 1):
    k = (3 * d - 1)//7
    if closest[0] * d < closest[1] * k:
        closest[0], closest[1] = k, d
print(closest[0])