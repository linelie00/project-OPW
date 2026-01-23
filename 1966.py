from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    paper = list(map(int, input().split()))
    
    que = deque(enumerate(paper))
    cnt = 0

    while que:
        x = que.popleft()
        max_value = max(v for _, v in que) if que else 0

        if x[1] >= max_value:
            cnt += 1
            if x[0] == m:
                print(cnt)
                break
        else:
            que.append(x)
