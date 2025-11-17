from itertools import combinations

n, m = map(int,input().split())
for i in combinations(range(1,n+1),m):
    print(*i) #괄호없이 출력