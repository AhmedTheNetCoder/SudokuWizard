import pygame
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

width = 540
height = 600
cell_size = 60
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver")

font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 20)

grid = [[0 for _ in range(9)] for _ in range(9)]
user_filled = [[False for _ in range(9)] for _ in range(9)] 
invalid_cells = set() 

def draw_grid():
    dis.fill(WHITE)

    for i in range(9):
        for j in range(9):
            if grid[j][i] != 0: 
                color = BLACK if user_filled[j][i] else BLUE
                if (j, i) in invalid_cells: 
                    color = RED
                text = font.render(str(grid[j][i]), True, color)
                dis.blit(text, (i * cell_size + 20, j * cell_size + 10))

    for i in range(0, 10):
        line_thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(dis, BLACK, (i * cell_size, 0), (i * cell_size, 540), line_thickness)
        pygame.draw.line(dis, BLACK, (0, i * cell_size), (540, i * cell_size), line_thickness)

def highlight_cell(row, col):
    pygame.draw.rect(dis, LIGHT_BLUE, (col * cell_size, row * cell_size, cell_size, cell_size), 5)

def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(dis, color, (x, y, width, height))
    text_surface = small_font.render(text, True, text_color)
    dis.blit(text_surface, (x + (width / 2 - text_surface.get_width() / 2), y + (height / 2 - text_surface.get_height() / 2)))

    return pygame.Rect(x, y, width, height)  

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def validate_input(board):
    global invalid_cells
    invalid_cells.clear()  

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0 
                if not is_valid(board, row, col, num):
                    invalid_cells.add((row, col))  
                board[row][col] = num 

    return len(invalid_cells) == 0  

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        draw_grid()
                        pygame.display.update()
                        pygame.time.delay(50) 
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  
                return False
    return True

def main():
    running = True
    selected_cell = None
    solving = False

    while running:
        dis.fill(WHITE)
        draw_grid()

        solve_button_rect = draw_button("Start Solving", 200, 550, 140, 40, BLUE, WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if solve_button_rect.collidepoint(pos): 
                    if validate_input(grid):  
                        solving = True 
                    else:
                        solving = False  
                else:
                    x, y = pos
                    if x < 540 and y < 540:
                        selected_cell = (y // cell_size, x // cell_size)

            if event.type == KEYDOWN:
                if selected_cell and event.key in range(K_1, K_9 + 1):
                    grid[selected_cell[0]][selected_cell[1]] = event.key - K_0
                    user_filled[selected_cell[0]][selected_cell[1]] = True 
                elif selected_cell and event.key == K_BACKSPACE: 
                    grid[selected_cell[0]][selected_cell[1]] = 0
                    user_filled[selected_cell[0]][selected_cell[1]] = False 

        if selected_cell:
            highlight_cell(selected_cell[0], selected_cell[1])

        if solving:
            solve_sudoku(grid)
            solving = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
