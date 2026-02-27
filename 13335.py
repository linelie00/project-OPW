from collections import deque

n,w,L = map(int,input().split())
t = deque(map(int,input().split()))
time = 0
que = deque() #다리
weight = 0

while True:
    time += 1
    if que and time - que[0][1] >= w:
        truck,_ = que.popleft()
        weight -= truck
    if t and weight + t[0] <= L:
        weight += t[0]
        que.append((t.popleft(),time))
    
    
    if not t and not que:
        break
    print(que,t,time)
    
print(time)