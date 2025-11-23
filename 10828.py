from collections import deque
import sys

n = int(input())
dq = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        if dq:
            print(dq.popleft())
        else: print('-1')
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq: print('0')
        else: print('1')
    elif cmd[0] == 'top':
        if dq:
            print(dq[0])
        else: print('-1')
