import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    f_que = deque()
    s_que = deque()
    f_dist = [[-1]*w for _ in range(h)]
    s_dist = [[-1]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maze[i][j] == '*':
                f_que.append((i,j))
                f_dist[i][j] = 1
            elif maze[i][j] == '@':
                s_que.append((i,j))
                s_dist[i][j] = 1
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    print(1)
                    return
    
    while f_que:
        x,y = f_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and maze[nx][ny] != '#' and f_dist[nx][ny] == -1:
                f_dist[nx][ny] = f_dist[x][y] + 1
                f_que.append((nx,ny))

    while s_que:
        x,y = s_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and maze[nx][ny] != '#' and s_dist[nx][ny] == -1 and (f_dist[nx][ny] > s_dist[x][y]+1 or f_dist[nx][ny] == -1):
                s_dist[nx][ny] = s_dist[x][y] + 1
                if nx == 0 or nx == h-1 or ny == 0 or ny == w-1:
                    print(s_dist[nx][ny])
                    return
                s_que.append((nx,ny))
    print('IMPOSSIBLE')


for _ in range(T):
    w,h = map(int,input().split())
    maze = [list(input().strip()) for _ in range(h)]
    bfs()
