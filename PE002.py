def PE002(limit):
    fib1 = 1
    fib2 = 2
    total = 0
    while fib2 < limit:
        if fib2 % 2 == 0:
            total += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return total
print(PE002(4000000))