import sys
input = sys.stdin.readline

sudoku = [list(map(int,input().strip())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(x,y,num):
    for i in range(9):
        if sudoku[x][i] == num or sudoku[i][y] == num:
            return False
    
    for i in range(3):
        for j in range(3):
            if sudoku[x//3*3+i][y//3*3+j] == num:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for row in sudoku:
            print(*row)
        exit()
    
    for num in range(1,10):
        x, y = blank[idx]
        if check(x,y,num):
            sudoku[x][y] = num
            dfs(idx+1)
            sudoku[x][y] = 0

dfs(0)