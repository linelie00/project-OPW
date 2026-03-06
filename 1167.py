import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(V):
    arr = list(map(int,input().split()))
    node = arr[0]
    for j in range(1,len(arr),2):
        if arr[j] == -1:
            break
        graph[node].append((arr[j],arr[j+1]))

def bfs(idx):
    dist = [-1]*(V+1)
    dist[idx] = 0
    que = deque([idx])

    while que:
        x = que.popleft()
        for nx,w in graph[x]:
            if dist[nx] ==-1:
                dist[nx] = dist[x] + w
                que.append(nx)
    
    max_v = max(dist)
    max_i = dist.index(max_v)

    return max_v,max_i

_,i = bfs(1)
v,_ = bfs(i)

print(v)