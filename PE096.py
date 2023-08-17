def checkNum(row, col, num):
    for y in range(9):
        if grid[row][y] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solve(row, col):

    if (row == 8 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] != 0:
        return solve(row, col + 1)

    for num in range(1, 10):
        if checkNum(row, col, num):
            grid[row][col] = num
            if solve(row, col + 1):
                return True
        grid[row][col] = 0
    return False

contents = open("PE096.txt").read().splitlines()
start = 1
end = 10
total = 0
for _ in range(1, 51):
    grid = [[int(j) for j in i] for i in contents[start:end]]
    solve(0, 0)
    total += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
    start += 10
    end += 10
print(total)
