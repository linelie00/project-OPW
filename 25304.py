x = int(input())
n = int(input())
for _ in range(n):
    p,q = map(int,input().split())
    x -= p*q
if x == 0:
    print('Yes')
else:
    print('No')