import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pokemon = {}
for i in range(1,N+1):
    p = input().rstrip()
    pokemon[i] = p
    pokemon[p] = i
for _ in range(M):
    p = input().rstrip()
    if p.isdigit():
        print(pokemon[int(p)])
    else:
        print(pokemon[p])