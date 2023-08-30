import random
import time
import os

def initialize_grid(rows, cols, density=0.2):
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal
    for row in grid:
        print(' '.join(['■' if cell else '□' for cell in row]))
    print()

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
    rows = 30
    cols = 60
    steps = 50
    density = 0.2
    main(rows, cols, steps, density)
