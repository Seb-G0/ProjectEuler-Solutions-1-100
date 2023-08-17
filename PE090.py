from itertools import combinations
squares = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
cube = list(combinations([0,1,2,3,4,5,6,7,8,6], 6))

def isSolution(d1, d2):
    return all(x in d1 and y in d2 or x in d2 and y in d1 for x, y in squares)
count = 0
for i,d1 in enumerate(cube):
    for d2 in cube[:i]:
        if isSolution(d1, d2):
            count += 1

print(count)
