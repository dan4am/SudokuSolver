# 1. Description.



Sudoku solver is a project encompasses 3 sub-projects:

	1. A sudoku game and a solver.
    2. An android solver (requires adb)
    3. A sudoku generator that reads the screen of an android device.
    
## Prerequisites

- python 3.9
- pygame 2.0.1
- opencv-python 4.5
- pytesseract 0.3.7
- numpy 1.20.3


To launch the scripts, execute in a command prompt:

`python3 main_with_multiprocessing`

or

`python3 main_with_multithreading`

this litle GUI will appear 

![image](https://user-images.githubusercontent.com/39918471/129459894-9931edde-efdb-49ef-8a0c-22b8901ead5c.png)

  
## 1.1. Sudoku game + solver.

The sudoku game is a classic sudoku game, each time it is launched it starts with different grid chosen in a database of over **1 million** grids.
![image](https://user-images.githubusercontent.com/39918471/129459929-c4f90a6c-b89d-4bab-b265-78b73eae3f65.png)


The solver algorithm is an customized iterative Crosshatching algorithm that fills x number of cases at each iteration.
For all the empty cases of a given line, column or sub-grid of the sudoku grid, the algorithm tries each number from 1 to nine and fill the case with a number iff the number is the only possible solution.

![Crosshathing illustration.](image2.png)
## a. commands

`esc` → Clear the grid.

`s` → Launch the solver.

`r` → Load a random grid.
## 1.2. Android solver.

## 1.3. Android sudoku generator.
