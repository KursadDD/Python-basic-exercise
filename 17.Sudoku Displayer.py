PROBLEM:
The department you work for has received a project that displays the solved sudoku puzzles in a digital environment. 

Write a Python code to print out the given sudoku puzzle matrix in the following format.
Given format :
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
Desired output format :
- - - - - - - - - - - - - - - 
0  0  0  | 0  6  4  | 0  0  0  
7  0  0  | 0  0  0  | 3  9  0  
8  0  0  | 0  0  0  | 0  0  0  
- - - - - - - - - - - - - - - 
0  0  0  | 5  0  2  | 0  6  0  
0  8  0  | 4  0  0  | 0  0  0  
3  5  0  | 6  0  0  | 0  7  0  
- - - - - - - - - - - - - - - 
0  0  2  | 0  0  0  | 1  0  3  
0  0  1  | 0  5  9  | 0  0  0  
0  0  0  | 0  0  0  | 7  0  0  
- - - - - - - - - - - - - - -

SOLUTİON:
import os
os.system("cls")
import sys

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
for j in range(0,9):

    print()    
    if j == 0 or j == 3 or j == 6:
        print("---------------------")
    for i in range(0,9,3):
        print(sudoku[j][i], sudoku[j][i+1], sudoku[j][i+2], end="")
        if i == 0 or i == 3:
            print(end=" | ")
print()
print("---------------------")        