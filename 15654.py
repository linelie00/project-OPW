from itertools import permutations

N,M = map(int,input().split())
num = sorted(list(map(int,input().split())))

for x in permutations(num,M):
    print(*x)