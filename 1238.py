from collections import deque

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    rev_graph[b].append((a,t))

INF = 10**100

dist_out = [INF]*(N+1)
dist_in = [INF]*(N+1)

que = deque()
que.append(X)
dist_out[X] = 0

while que:
    x = que.popleft()
    for i,t in graph[x]:
        if dist_out[i] > dist_out[x] + t:
            dist_out[i] = dist_out[x] + t
            que.append(i)

que.append(X)
dist_in[X] = 0

while que:
    x = que.popleft()
    for i,t in rev_graph[x]:
        if dist_in[i] > dist_in[x] + t:
            dist_in[i] = dist_in[x] + t
            que.append(i)

answer = 0
for i in range(1,N+1):
    answer = max(answer,dist_in[i]+dist_out[i])

print(answer)