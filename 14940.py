import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

que = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            que.append((i,j))
            dist[i][j] = 0

while que:
    x,y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y]+1
            que.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()