n = int(input())
tower = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and stack[-1][0] <= tower[i]:
        stack.pop()
    if stack:
        print(stack[-1][1]+1, end=" ")
    else:
        print('0', end=" ")
    stack.append((tower[i],i))