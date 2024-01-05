t = int(input())
high_score = 0
for i in range(t):
    a,b,c = map(int,input().split())
    if a==b==c: score = 10000+a*1000
    elif a==b or a==c: score = 1000+a*100
    elif b==c: score = 1000+b*100
    else: score = max(a,b,c)*100
    
    if score > high_score:
        high_score = score

print(high_score)
