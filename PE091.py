
def isrt(x1, y1, x2, y2, x3 = 0, y3 = 0):

    sidea = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    sideb = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)
    sidec = (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)

    return (sidea + sideb == sidec) or (sidea + sidec == sideb) or (sideb + sidec == sidea)

count = 0
points = set()
for x1 in range(51):
    for x2 in range(x1, 51):
        for y2 in range(51):
            for y1 in range(y2, 51):
                if isrt(x1, y1, x2, y2) and not((x1 == x2 and y1 == y2) or (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0)):
                    count += 1
print(count)