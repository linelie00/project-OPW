import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

ops = {
    'D': lambda x: (x*2)%10000,
    'S': lambda x: (x-1)%10000,
    'L': lambda x: (x % 1000) * 10 + x // 1000,
    'R': lambda x: (x % 10) * 1000 + x // 10
}

for _ in range(T):
    visited = [False]*10000
    prev = [-1]*10000
    how = ['']*10000

    a,b = map(int,input().split())
    que = deque([a])
    visited[a] = True

    while que:
        x = que.popleft()

        if x == b:
            break

        for op in ops:
            nx = ops[op](x)

            if not visited[nx]:
                visited[nx] = True
                prev[nx] = x
                how[nx] = op
                que.append(nx)
    ans = []
    cur = b

    while cur != a:
        ans.append(how[cur])
        cur = prev[cur]

    print(''.join(ans[::-1]))