n = int(input())
arr = [int(input()) for _ in range(n)]
stack = [0]
anw = []
last = 0

for i in arr:
    if i == stack[-1]:
        stack.pop()
        anw.append('-')
    elif i in stack:
        print('NO')
        anw = []
        break
    else:
        for j in range(last+1,i,1):
            stack.append(j)
            anw.append('+')
        anw.append('+')
        anw.append('-')
        last = i
if anw:
    for i in anw:
        print(i)