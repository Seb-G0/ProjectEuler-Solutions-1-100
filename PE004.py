def ispalindrome(num):
    num = str(num)
    if len(num) == 1:
        return False
    if num[0] != num[-1]:
        return False
    elif len(num) == 2:
        return True
    else:
        return ispalindrome(num[1:-1])

def solve():
    products = []
    for num1 in range(101, 1000):
        for num2 in range(num1, 1000):
            products.append(num1 * num2)
    products.sort()
    products.reverse()
    for p in products:
        if ispalindrome(p):
            return p

print(solve())