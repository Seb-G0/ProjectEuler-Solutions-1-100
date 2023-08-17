def generateTriangles(n):
    res = []
    t = 1
    while 1/2 * t * (t+1) < n:
        res.append(1/2 * t * (t+1))
        t += 1
    return res

contents = open('PE042.txt').read()
contents = contents.split('","')
alpha = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
trianglenums = generateTriangles(26 * 10)
for word in contents:
    total = sum([alpha.find(letter) for letter in word])
    if total in trianglenums:
        count += 1
print(count)