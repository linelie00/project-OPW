N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
M = int(input())
cnt = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    global cnt
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

visited[1] = True
dfs(1)
print(cnt)