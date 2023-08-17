def PE006(limit):
    total = 0
    sum = 0
    for i in range(1, limit + 1):
        total += i * i
        sum += i
    return sum * sum - total
print(PE006(100))