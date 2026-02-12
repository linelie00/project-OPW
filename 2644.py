N = int(input())
A,B = map(int,input().split())
M = int(input())
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n,cnt):
    if graph[n]:
        for x in graph[n]:
            if not visited[x]:
                visited[x] = True
                if x == B:
                    print(cnt)
                    exit()
                dfs(x,cnt+1)
visited[A] = True
dfs(A,1)
print(-1)