n = int(input())
stack = []
cnt = 0
for i in range(n):
    h = int(input())
    while stack and stack[-1] <= h:
        stack.pop()
    cnt += len(stack)
    stack.append((h))
print(cnt)