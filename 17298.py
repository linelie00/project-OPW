n = int(input())
arr = list(map(int,input().split()))
stack = []
ans = [-1]*(n)

for i in range(n):
    while stack and stack[-1][1] < arr[i]:
        ans[stack.pop()[0]] = arr[i]
    stack.append((i, arr[i]))
print(*ans)