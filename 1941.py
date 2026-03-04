from collections import deque

graph = [list(input()) for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def bfs(selected):
    x,y = selected[0]
    que = deque([(x,y)])

    visited = [[False]*5 for _ in range(5)]
    visited[x][y] = True

    cnt = 1

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and (nx,ny) in selected:
                visited[nx][ny] = True
                cnt += 1
                que.append((nx,ny))
    if cnt == 7:
        return True
    else:
        return False

def dfs(idx,selected,s_cnt):
    global ans

    if len(selected) - s_cnt >= 4:
        return

    if len(selected) == 7:
        if bfs(selected):
            ans += 1
        return
    
    for i in range(idx,25):
        x = i//5
        y = i%5
        if graph[x][y] == 'S':
            dfs(i+1,selected+[(x,y)],s_cnt+1)
        else:
            dfs(i+1,selected+[(x,y)],s_cnt)

dfs(0, [], 0)
print(ans)