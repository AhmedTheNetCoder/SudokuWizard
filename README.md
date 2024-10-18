# Sudoku Solver

This is a Sudoku solver built with Python and Pygame. You can input your Sudoku puzzle by clicking on cells and typing numbers. Once done, press "Start Solving" to solve the puzzle automatically. The solver validates your inputs and highlights any invalid entries in red.

## How to Play
1. Click on any cell in the grid to select it.
2. Type a number (1-9) to fill the selected cell.
3. If you make a mistake, you can clear the cell by pressing Backspace.
3. Once your puzzle is complete, press "Start Solving" to solve it automatically.
4. If there are invalid entries (duplicate numbers in the same row, column, or 3x3 sub-grid), they will be highlighted in red. Correct these before solving.
5. The solution will be shown with the solved numbers appearing in blue, so you can distinguish between the numbers you entered and those the solver completed.

## Validation

1. The program checks for duplicate numbers in rows, columns, and 3x3 sub-grids.
2. If any violations are detected, the corresponding cells will be highlighted in red when you press "Start Solving."
3. You must correct the invalid entries before the solver can proceed.

## How to Run

Run the SudokuWizard.py file

## Requirements
- Python 3.x
- Pygame (`pip install pygame`)
