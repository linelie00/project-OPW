import sys
input = sys.stdin.readline

H, W = map(int, input().split())
r, c, d = map(int, input().split())

ruleA = [list(map(int, input().strip())) for _ in range(H)]
ruleB = [list(map(int, input().strip())) for _ in range(H)]

clean = [[False] * W for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[[False] * W for _ in range(H)] for _ in range(4)]

move_cnt = 0
not_clean_move = 0
answer = 0

while not visited[d][r][c]:

    if not clean[r][c]:
        clean[r][c] = True

        answer += 1 + not_clean_move
        not_clean_move = 0

        visited = [[[False] * W for _ in range(H)] for _ in range(4)]

        d = (d + ruleA[r][c]) % 4

    else:
        visited[d][r][c] = True
        not_clean_move += 1
        d = (d + ruleB[r][c]) % 4

    nr = r + dx[d]
    nc = c + dy[d]

    if not (0 <= nr < H and 0 <= nc < W):
        break

    r, c = nr, nc

print(answer)