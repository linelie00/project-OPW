import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, visited):
    que = deque([(x,y)])
    visited[x][y] = True
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx,ny))

def melt():
    melt_amount = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0<=ni<N and 0<=nj<M and graph[ni][nj] == 0:
                        cnt += 1
                melt_amount[i][j] = cnt
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                graph[i][j] = max(0, graph[i][j] - melt_amount[i][j])

year = 0

while True:
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1
    
    if cnt >= 2:
        print(year)
        break
    
    if cnt == 0:
        print(0)
        break
    
    melt()
    year += 1