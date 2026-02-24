from collections import deque

F,S,G,U,D = map(int,input().split())
dist = [-1]*(F+1)
que = deque()
que.append(S)
dist[S] = 0

while que:
    x = que.popleft()
    if x == G:
        print(dist[-1])
        exit()
    ux = x+U
    if 1<=ux<=F and dist[ux] == -1:
        dist[ux] = dist[x]+1
        que.append(ux)
    dx = x-D
    if 1<=dx<=F and dist[dx] == -1:
        dist[dx] = dist[x]+1
        que.append(dx)
print('use the stairs')