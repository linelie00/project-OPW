n = int(input())
x,y = map(int,input().split())
array = [x,y]
for i in range(n):
    k = input()
    if k == 'W':
        array[0] += 1
    if k == 'D':
        array[1] += 1
    if k == 'A':
        array[1] -= 1 
    if k == 'S':
        array[0] -= 1

print(array[0], array[1])
