import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire = [[-1] * c for _ in range(r)]
dist = [[-1] * c for _ in range(r)]

fire_q = deque()
jihun_q = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fire_q.append((i, j))
            fire[i][j] = 0
        elif maze[i][j] == 'J':
            jihun_q.append((i, j))
            dist[i][j] = 0

while fire_q:
    x, y = fire_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if maze[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                fire_q.append((nx, ny))

while jihun_q:
    x, y = jihun_q.popleft()

    if x == 0 or x == r - 1 or y == 0 or y == c - 1:
        print(dist[x][y] + 1)
        sys.exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if maze[nx][ny] == '.' and dist[nx][ny] == -1:
                if fire[nx][ny] == -1 or fire[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    jihun_q.append((nx, ny))

print("IMPOSSIBLE")
