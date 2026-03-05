N,M = map(int,input().split())

a = set([input() for _ in range(N)])
b = set([input() for _ in range(M)])

ans = sorted(list(a&b))

print(len(ans))
for x in ans:
    print(x)