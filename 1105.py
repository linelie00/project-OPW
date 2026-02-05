import sys
input = sys.stdin.readline

l,r = map(str, input().split())

if len(l) != len(r):
    print(0)
    exit()
cnt = 0
for i in range(len(l)):
    if l[i] == r[i]:
        if l[i] == '8':
            cnt += 1
    else:
        break

print(cnt)