from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상어 초기 상태
size = 2
eaten = 0
time = 0

# 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            graph[i][j] = 0

# 방향: 상, 좌, 우, 하 (위/왼쪽 우선 보장)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

while True:
    visited = [[-1] * n for _ in range(n)]
    que = deque()
    
    visited[sx][sy] = 0
    que.append((sx, sy))
    
    fish = []

    # BFS
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        fish.append((visited[nx][ny], nx, ny))

    # 먹을 물고기 없음 → 종료
    if not fish:
        break

    # 가장 가까운 물고기 선택
    fish.sort()
    dist, fx, fy = fish[0]

    # 이동 및 상태 갱신
    time += dist
    sx, sy = fx, fy
    graph[fx][fy] = 0

    eaten += 1
    if eaten == size:
        size += 1
        eaten = 0

print(time)