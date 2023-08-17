contents = open('PE022.txt').read().split('","')
contents.sort()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = 0
for i in contents:
    total = 0
    for letter in i:
        num = alpha.find(letter) + 1
        num = num * (contents.index(i) + 1)
        total += num
    s += total
print(s)