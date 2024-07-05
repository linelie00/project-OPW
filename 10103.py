n = int(input())
a_score = 100
b_score = 100
for i in range(n):
    a,b = map(int, input().split())
    if a<b: a_score -= b
    elif a>b: b_score -= a
print(a_score)
print(b_score)