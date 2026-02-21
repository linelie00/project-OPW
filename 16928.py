from collections import deque

N,M = map(int,input().split())
move = [0]*101
dist = [-1]*101
for _ in range(N+M):
    a,b = map(int,input().split())
    move[a] = b

que = deque()
que.append(1)
dist[1] = 0

while que:
    x = que.popleft()
    for i in range(1,7):
        nx = x+i
        if nx > 100:
            continue

        if move[nx]:
            nx = move[nx]

        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            que.append(nx)

print(dist[100])