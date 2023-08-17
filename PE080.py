
#https://studylib.net/doc/7921494/square-roots-by-subtraction---jarvis--frazer
def PE080(n):
    a = 5 * n
    b = 5
    while b < 10 ** 102:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b // 10) * 100 + 5
    return int(str(b)[:100])


total = 0
for n in range(2, 101):
    if int(n ** 0.5) == n ** 0.5:
        continue
    total += sum([int(d) for d in str(PE080(n))])
print(total)
