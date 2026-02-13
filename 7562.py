from collections import deque

T = int(input())

dx = [2,2,1,-1,-2,-2,1,-1]
dy = [1,-1,2,2,1,-1,-2,-2]

def bfs():
    dist = [[-1]*l for _ in range(l)]
    que = deque([(sx, sy)])
    dist[sx][sy] = 0

    while que:
        x, y = que.popleft()
        if x == ex and y == ey:
            print(dist[x][y])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))


for _ in range(T):
    l = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())

    bfs()