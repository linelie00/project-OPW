from collections import deque

while True:
    s = input().strip()
    if s == '0':
        break

    n = deque(s)

    for _ in range(len(n) // 2):
        if n.pop() != n.popleft():
            print('no')
            break
    else:
        print('yes')