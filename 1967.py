from collections import deque

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,w = map(int,input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))

def bfs(start):
    dist = [-1]*(n+1)
    que = deque([start])
    dist[start] = 0

    while que:
        x = que.popleft()
        for nx,w in edges[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + w
                que.append(nx)
    
    far_dist = max(dist)
    far_node = dist.index(far_dist)
    
    return far_node, far_dist

u,_ = bfs(1)
_,diameter = bfs(u)

print(diameter)