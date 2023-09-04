import random
import sys
import time
import os

LIVE_CELL = '\u2b1b'
DEAD_CELL = '\u2b1c'

NEIGHBOR_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def initialize_grid(rows=20, cols=40, density=0.2):
    grid = [[random.choices([0, 1], [1 - density, density])[0] for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join([LIVE_CELL if cell else DEAD_CELL for cell in row]))

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx, dy in NEIGHBOR_DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx][ny]
    return count

def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
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
    rows = 20
    cols = 40
    steps = 200
    density = 0.2
    main(rows, cols, steps, density)
