n = list(map(int, input().split()))
print(sum([n[i]**2 for i in range(5)])%10)