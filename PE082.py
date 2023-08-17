def PE082(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        memo[i][0] = matrix[i][0]

    for j in range(1, cols):
        for i in range(rows):
            memo[i][j] = memo[i][j - 1] + matrix[i][j]
        for i in range(1, rows):
            memo[i][j] = min(memo[i][j], memo[i - 1][j] + matrix[i][j])
        for i in range(rows - 2, -1, -1):
            memo[i][j] = min(memo[i][j], memo[i + 1][j] + matrix[i][j])

    min_sum = min(memo[i][-1] for i in range(rows))
    return min_sum

matrix = [[int(i) for i in line.split(',')] for line in open("PE081.txt").read().splitlines()]


print(PE082(matrix))


