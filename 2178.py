import sys
from collections import deque

input = sys.stdin.readline

def bfs(maze,x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                    que.append((nx, ny)) 
                    maze[nx][ny] = maze[x][y] + 1
    return maze[n-1][m-1]
    

n,m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(maze,0,0))