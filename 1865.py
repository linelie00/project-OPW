T = int(input())

for _ in range(T):
    n,m,w = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        s,e,t = map(int,input().split())
        graph[s-1].append((e-1,t))
        graph[e-1].append((s-1,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        graph[s-1].append((e-1,-t))
    
    dist = [0]*n

    cycle = False

    for i in range(n): #노드 수만큼 반복
        for u in range(n):
            for v,cost in graph[u]: # u->v로 가는게 기존에 저장된 v경로보다 빠르다면 업데이트
                if dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    if i == n-1:
                        cycle = True

    if cycle:
        print("YES")
    else:
        print("NO")