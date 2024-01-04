t = int(input())
for j in range(t):
    a,b = map(int,input().split())
    anw = a*b
    while b != 0:
        r = a % b
        a = b
        b = r
    print(anw//a)
