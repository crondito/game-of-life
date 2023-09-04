import random
import time
import os

custom_grid_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

custom_grid_2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

custom_grid_3 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

custom_grid_4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

LIVE_CELL = '\u2b1b'
DEAD_CELL = '\u2b1c'

NEIGHBOR_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def initialize_grid(rows=20, cols=40, density=0.2):
    grid = [[random.choices([0, 1], [1 - density, density])[0] for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid, step):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join([LIVE_CELL if cell else DEAD_CELL for cell in row]))
    print(f"Paso {step}")

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

def get_user_input():
    print("Bienvenido al JUEGO DE LA VIDA")
    print("Opciones:")
    print("1. Cuadrícula al azar [filas=20, columnas=40, pasos=200, densidad=0.2]")
    print("2. Ejemplo Oscilador")
    print("3. Ejemplo Nave espacial")
    print("4. Ejemplo Estático")
    print("5. Ejemplo Matusalen (Die Hard)")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        return 20, 40, 200
    elif choice == "2":
        return len(custom_grid_1), len(custom_grid_1[0]), 100
    elif choice == "3":
        return len(custom_grid_2), len(custom_grid_2[0]), 50
    elif choice == "4":
        return len(custom_grid_3), len(custom_grid_3[0]), 20
    elif choice == "5":
        return len(custom_grid_4), len(custom_grid_4[0]), 60
    else:
        print("Invalid choice. Using option 1.")
        time.sleep(3)
        return 20, 40, 200

def main(grid=None):
    if grid is None:
        rows, cols, steps = get_user_input()
        if rows == len(custom_grid_1) and cols == len(custom_grid_1[0]):
            grid = custom_grid_1
        elif rows == len(custom_grid_2) and cols == len(custom_grid_2[0]):
            grid = custom_grid_2
        elif rows == len(custom_grid_3) and cols == len(custom_grid_3[0]):
            grid = custom_grid_3
        elif rows == len(custom_grid_4) and cols == len(custom_grid_4[0]):
            grid = custom_grid_4
        else:
            grid = initialize_grid(rows, cols)
    
    for step in range(1, steps + 1):
        print_grid(grid, step)
        grid = update_grid(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
