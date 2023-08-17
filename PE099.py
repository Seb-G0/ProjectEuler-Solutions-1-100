from math import log
mx = [0, 0]
contents = open("PE099.txt").read().splitlines()
for i, line in enumerate(contents):
    base, exp = line.split(',')
    base, exp = int(base), int(exp)
    if int(exp) * log(int(base)) > mx[0]:
        mx = [exp * log(base), i + 1]
print(mx[1])
