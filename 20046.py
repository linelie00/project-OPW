import sys
import heapq as hq
input = sys.stdin.readline

n,m = map(int, input().split())
icp = [list(map(int, input().split())) for _ in range(n)]
INF = 10**15
dist = [[INF]*m for _ in range(n)]
# 0: 단위 도로 이미 존재
# 1: 단위 도로가 없고 1의 비용으로 건설 가능
# 2: 단위 도로가 없고 2의 비용으로 건설 가능
# -1: 단위 도로를 건설할 수 없는 상태
# 맨 왼쪽 위에서 오른쪽 아래로 가는 경로를 만들기 위한 최소 건설 비용

if icp[0][0] == -1:
    print(-1)
    exit()

dist[0][0] = icp[0][0]
pq = []
hq.heappush(pq, (dist[0][0], 0, 0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while pq:
    cost,x,y = hq.heappop(pq)

    if cost > dist[x][y]:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and icp[nx][ny] != -1:
            next_cost = cost + icp[nx][ny]
            if next_cost < dist[nx][ny]:
                dist[nx][ny] = next_cost
                hq.heappush(pq, (next_cost, nx, ny))

if dist[-1][-1] == INF:
    print(-1)
else:
    print(dist[-1][-1])