N = int(input())
graph = [[0]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find(p,likes):
    global graph
    candidates = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0:
                continue
            blank = 0
            friend = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if graph[nx][ny] == 0:
                        blank += 1
                    elif graph[nx][ny] in likes:
                        friend += 1
            candidates.append((friend, blank, -x, -y))
    candidates.sort(reverse=True)
    _, _, rx, ry = candidates[0]
    graph[-rx][-ry] = p

likes_info = {}

for _ in range(N*N):
    s = list(map(int,input().split()))
    likes_info[s[0]] = s[1:]
    find(s[0],s[1:])

score = 0
for x in range(N):
    for y in range(N):
        student = graph[x][y]
        cnt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] in likes_info[student]:
                    cnt += 1

        if cnt > 0:
            score += 10 ** (cnt - 1)
print(score)