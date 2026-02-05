m = int(input())
s = set()
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in s else 0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else: s.add(int(cmd[1]))
    elif cmd[0] == 'all':
        s = set([i for i in range(1,21)])
    elif cmd[0] == 'empty':
        s = set()