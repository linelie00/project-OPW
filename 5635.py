n = int(input())
arr = []

for _ in range(n):
    name, d, m, y = input().split()
    arr.append([name, int(d), int(m), int(y)])
    
young = arr[0]
old = arr[0]
for i in range(1, n):
    temp = arr[i]
    if temp[3] > young[3] or (temp[3] == young[3] and temp[2] > young[2]) or (temp[3] == young[3] and temp[2] == young[2] and temp[1] > young[1]):
        young = temp
    elif temp[3] < old[3] or (temp[3] == old[3] and temp[2] < old[2]) or (temp[3] == old[3] and temp[2] == old[2] and temp[1] < old[1]):
        old = temp
print(young)
print(old)