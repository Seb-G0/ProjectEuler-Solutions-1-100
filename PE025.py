fib1, fib2, index = 1, 2, 3
while len(str(fib2)) < 1000:
    fib1, fib2 = fib2, fib1 + fib2
    index += 1
print(index)