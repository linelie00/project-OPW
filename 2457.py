import sys
input = sys.stdin.readline

N = int(input())
flowers = [list(map(int,input().split())) for _ in range(N)]
flowers.sort()

cnt = 0
cur_m, cur_d = 3, 1
idx = 0
best_end = (0, 0)

while (cur_m, cur_d) < (12, 1):
    found = False

    while idx < N:
        sm, sd, em, ed = flowers[idx]
        if (sm, sd) <= (cur_m, cur_d):
            if (em, ed) > best_end:
                best_end = (em, ed)
                found = True
            idx += 1
        else:
            break

    if not found:
        print(0)
        exit()

    cnt += 1
    cur_m, cur_d = best_end

print(cnt)