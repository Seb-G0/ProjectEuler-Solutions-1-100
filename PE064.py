def find_period(n):
    if int(n ** 0.5) == n ** 0.5:
        return 0
    m = 0
    d = 1
    a = int(n ** 0.5)
    initial_a = a
    period = 0
    while a != 2 * initial_a:
        m = d * a - m
        d = (n - m * m) // d
        a = (initial_a + m) // d
        period += 1
    return period

count = 0
for i in range(2, 10001):
    v = find_period(i)
    if v:
        if v % 2 == 1:
            count += 1
print(count)