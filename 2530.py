a,b,c = map(int,input().split())
d = int(input())
c+=d
b+=c//60
print(f"{(a+(b//60))%24} {b%60} {c%60}")
