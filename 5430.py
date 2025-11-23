from collections import deque

t = int(input())

for _ in range(t):
    cmd = list(input())
    n = int(input())
    arr = input().strip()
    if n == 0:
        dq = deque()
    else:
        dq = deque(arr[1:-1].split(','))
    r = False
    err = False
    for i in cmd:
        if i == 'R':
            r = not r
        else:
            if dq:
                if r:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print('error')
                err = True
                break
    if err:
        continue
    if r:
        dq.reverse()

    print("[" + ",".join(dq) + "]")