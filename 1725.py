import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = 0

for i in range(N):
    x = int(input())
    start = i
    while stack and stack[-1][1] > x:
        index,n = stack.pop()
        ans = max(ans,(i-index)*n)
        start = index
    stack.append([start,x])

while stack:
    index,n = stack.pop()
    ans = max(ans,(N-index)*n)

print(ans)