import sys
from collections import deque

input = sys.stdin.readline

N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)
anw_dfs = []
anw_bfs = []

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for row in graph:
    row.sort()

def dfs(v):
    visited_dfs[v] = True
    anw_dfs.append(v)
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    que = deque()
    que.append(v)
    anw_bfs.append(v)
    visited_bfs[v] = True
    while que:
        x = que.popleft()
        for i in graph[x]:
            if not visited_bfs[i]:
                que.append(i)
                anw_bfs.append(i)
                visited_bfs[i] = True

dfs(V)
print(*anw_dfs)
bfs(V)
print(*anw_bfs)