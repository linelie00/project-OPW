import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())

dist = [-1]*100001

que = deque([N])
dist[N] = 0

while que:
    x = que.popleft()

    if x == K:
        print(dist[x])
        break

    nx = x*2
    if 0<=nx<=100000 and dist[nx] == -1:
        dist[nx] = dist[x]
        que.append(nx)

    nx = x-1
    if 0<=nx<=100000 and dist[nx] == -1:
        dist[nx] = dist[x] + 1
        que.append(nx)

    nx = x+1
    if 0<=nx<=100000 and dist[nx] == -1:
        dist[nx] = dist[x] + 1
        que.append(nx)