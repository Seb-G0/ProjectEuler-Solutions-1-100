def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
def digitsum(n):
    return sum(int(i) for i in str(n))

print(digitsum(factorial(100)))