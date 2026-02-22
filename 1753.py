import sys
import heapq

input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

heap = []
heapq.heappush(heap,(0,K))
INF = 10**15
dist = [INF]*(V+1)
dist[K] = 0

while heap:
    d,u = heapq.heappop(heap)
    if d > dist[u]: #이미 더 짧은 거리로 갱신되었다면 무시
        continue
    for v,w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(heap, (dist[v], v))

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])