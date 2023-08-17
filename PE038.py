def builder(num):
    concat = ''
    for i in range(1,6):
        s = str(num * i)
        concat += s
        if len(concat) == 9:
            return concat
    return ''
def ispandigital(t):
    t = str(t)
    if '0' in t:
        return False
    return len(set(t)) == 9

for j in range(10000, 0, -1):
    t = builder(j)
    if ispandigital(t):
        print(t)
        break