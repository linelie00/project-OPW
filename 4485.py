import sys
from collections import deque

input = sys.stdin.readline

INF = 10**15
dx = [-1,1,0,0]
dy = [0,0,-1,1]
idx = 1

while True:
    N = int(input())
    if N == 0:
        exit()
    graph = [list(map(int,input().split())) for _ in range(N)]
    dist = [[INF]*N for _ in range(N)]
    que = deque()
    que.append((0,0))
    dist[0][0] = graph[0][0]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                    dist[nx][ny] = dist[x][y] + graph[nx][ny]
                    que.append((nx,ny))
    print(f"Problem {idx}: {dist[-1][-1]}")
    idx += 1