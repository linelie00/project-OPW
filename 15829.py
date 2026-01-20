n = int(input())
arr = list(input().strip())
anw = 0
for i in range(n):
    anw += (ord(arr[i])-96)*31**i % 1234567891
print(anw)