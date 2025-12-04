import sys
input = sys.stdin.readline

arr = list(input().strip())
stack = []
cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)