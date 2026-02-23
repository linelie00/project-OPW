import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(new_graph):
    que = deque(virus)
    cnt = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                que.append((nx,ny))
                cnt += 1
    return cnt

virus = []
blank = []
blank_cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 0:
            blank.append((i,j))
            blank_cnt +=1

max_safe = 0
comb = combinations(blank,3)
for (ax,ay),(bx,by),(cx,cy) in comb:
    new_graph = [row[:] for row in graph]
    new_graph[ax][ay] = 1
    new_graph[bx][by] = 1
    new_graph[cx][cy] = 1
    infected = bfs(new_graph)
    safe = blank_cnt - 3 - infected
    max_safe = max(max_safe, safe)
print(max_safe)