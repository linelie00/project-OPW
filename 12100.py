import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def left(board):
    for i in range(n):
        top = 0
        for j in range(1,n):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = temp
                elif board[i][top] == temp:
                    board[i][top] *= 2
                    top += 1
                else:
                    top += 1
                    board[i][top] = temp
    return board

def right(board):
    for i in range(n):
        top = n-1
        for j in range(n-2,-1,-1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = temp
                elif board[i][top] == temp:
                    board[i][top] *= 2
                    top -= 1
                else:
                    top -= 1
                    board[i][top] = temp
    return board

def up(board):
    for j in range(n):
        top = 0
        for i in range(1,n):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = temp
                elif board[top][j] == temp:
                    board[top][j] *= 2
                    top += 1
                else:
                    top += 1
                    board[top][j] = temp
    return board

def down(board):
    for j in range(n):
        top = n-1
        for i in range(n-2,-1,-1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = temp
                elif board[top][j] == temp:
                    board[top][j] *= 2
                    top -= 1
                else:
                    top -= 1
                    board[top][j] = temp
    return board

def dfs(n,arr):
    global ans
    if n == 5:
        for row in arr:
            for x in row:
                if x > ans: 
                    ans = x
        return
    for i in range(4):
        copy_arr = deepcopy(arr)
        if i == 0:
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else:
            dfs(n + 1, down(copy_arr))
dfs(0,board)
print(ans)