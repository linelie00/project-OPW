from collections import deque

n, m = map(int, input().split())
index = map(int, input().split())
q = deque([k for k in range(1,n+1)])
cnt = 0

for i in index:
    while True:
        if q[0] == i:
            q.popleft()
            break
        elif q.index(i) < len(q)/2:
            q.append(q.popleft())
            cnt += 1
        else:
            q.appendleft(q.pop())
            cnt += 1

print(cnt)