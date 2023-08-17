def PE005():
    values = [i for i in range(1, 21)]

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return abs(x)

    lcm = 1
    for n in values:
        lcm *= n // gcd(lcm, n)
    return lcm
print(PE005())