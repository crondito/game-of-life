import random
import sys
import time
import os

def initialize_grid(rows=20, cols=40, density=0.2):
    grid = [[random.choices([0, 1], [1 - density, density])[0] for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(['\u2b1b' if cell else '\u2b1c' for cell in row]).encode('utf-8').decode(sys.stdout.encoding))

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                count += grid[nx][ny]
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j]:
                new_grid[i][j] = 1 if 2 <= neighbors <= 3 else 0
            else:
                new_grid[i][j] = 1 if neighbors == 3 else 0
    return new_grid

def main(rows, cols, steps, density):
    grid = initialize_grid(rows, cols, density)
    for _ in range(steps):
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    rows = 40
    cols = 80
    steps = 300
    density = 0.2
    main(rows, cols, steps, density)
