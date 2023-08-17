def palindromatic(n):
    return n + int(str(n)[::-1])
def isPalindromatic(n):
    return str(n) == str(n)[::-1]

count = 0
for n in range(10, 10000):
    temp = True
    c = 0
    while temp and c < 50:
        value = palindromatic(n)
        if isPalindromatic(value):
            temp = False
            break
        n = value
        c += 1
    if temp:
        count += 1
print(count)