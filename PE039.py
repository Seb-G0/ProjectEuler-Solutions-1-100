def triangles(p):
    res = set()
    if p % 2 != 0:
        return 0
    else:
        for b in range(1, p // 2):
            a = p / 2 * ((p - 2 * b) / (p - b))
            if (a == int(a)):
                ab = tuple(sorted((int(a), b)))
                res.add(ab)
        return len(res)


# Driver Code
mx = [1, 0]
for p in range(4, 1001):
    value = triangles(p)
    if value > mx[0]: mx[0], mx[1] = value, p
print(mx[1])
