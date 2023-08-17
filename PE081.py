from functools import cache
matrix = [[int(i) for i in line.split(',')] for line in open("PE081.txt").read().splitlines()]
@cache
def PE081(y = 0, x = 0):
    if y > len(matrix) - 1 or x > len(matrix) - 1:
        return 2 ** 31
    elif y == len(matrix) - 1 and x == len(matrix)-1:
        return matrix[y][x]
    return matrix[y][x] + min(PE081(y, x+1), PE081(y+1, x))
print(PE081())

