import heapq

class Cell:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

def PE083(matrix):
    size = len(matrix)
    processed = [[False for _ in range(size)] for _ in range(size)]
    next_cells = []
    heapq.heappush(next_cells, Cell(0, 0, matrix[0][0]))
    while next_cells:
        cell = heapq.heappop(next_cells)
        if processed[cell.y][cell.x]:
            continue
        processed[cell.y][cell.x] = True
        if cell.x == size - 1 and cell.y == size - 1:
            return cell.weight
        if cell.x + 1 < size:
            heapq.heappush(next_cells, Cell(cell.x + 1, cell.y, cell.weight + matrix[cell.y][cell.x + 1]))
        if cell.y + 1 < size:
            heapq.heappush(next_cells, Cell(cell.x, cell.y + 1, cell.weight + matrix[cell.y + 1][cell.x]))
        if cell.y > 0:
            heapq.heappush(next_cells, Cell(cell.x, cell.y - 1, cell.weight + matrix[cell.y - 1][cell.x]))
        if cell.x > 0:
            heapq.heappush(next_cells, Cell(cell.x - 1, cell.y, cell.weight + matrix[cell.y][cell.x - 1]))
    return -1

matrix = [[int(i) for i in line.split(',')] for line in open("PE081.txt").read().splitlines()]
result = PE083(matrix)
print(result)

