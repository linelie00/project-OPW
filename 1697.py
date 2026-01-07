import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())
MAX = 10 ** 5
arr = [-1] * (MAX + 1)

ops = [
    lambda x: x - 1,
    lambda x: x + 1,
    lambda x: x * 2
]

que = deque()
que.append(n)
arr[n] = 0

while que:
    x = que.popleft()
    if x == k:
        print(arr[x])
        sys.exit()
    for op in ops:
        nx = op(x)
        if 0 <= nx < MAX and arr[nx] == -1:
            arr[nx] = arr[x] + 1
            que.append(nx)