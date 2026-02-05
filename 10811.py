n,m = map(int, input().split())
arr = [i for i in range(n+1)]
print(arr)
for _ in range(m):
    i,j = map(int, input().split())
    arr[i:j+1] = arr[i:j+1][::-1]
    print(arr)

for i in range(1,n+1):
    print(arr[i], end=' ')