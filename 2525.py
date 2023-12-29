a,b = map(int,input().split())
c = int(input())
b+=c
print(f"{(a+(b//60))%24} {b%60}")
