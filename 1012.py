import sys
from collections import deque

input = sys.stdin.readline

def bfs(field,x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((x,y))
    field[y][x] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 1:
                que.append((nx,ny))
                field[ny][nx] = 0

t = int(input())

for _ in range(t):
    m,n,k = map(int,input().split())
    field = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        field[y][x] = 1
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(field,j,i)
                cnt += 1
    print(cnt)