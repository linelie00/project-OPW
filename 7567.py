bowl = list(input())
l = 10
for i in range(1, len(bowl)):
    if bowl[i-1] == bowl[i]: l += 5
    else: l += 10
print(l)
