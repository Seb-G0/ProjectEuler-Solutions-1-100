def PE001(limit):
    total = 0
    for n in range(3, limit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total
print(PE001(1000))