n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    l = (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2
    r = (arr[2]+arr[5])**2
    if l == 0 and arr[2] == arr[5]:
        print(-1)
    elif l == r or l == (arr[2]-arr[5])**2 *2:
        print(1)
    elif l < r:
        print(2)
    else:
        print(0)