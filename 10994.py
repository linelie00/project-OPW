n = int(input())
mid = (n-1)*2

for i in range(mid*2+1):
    if i == 0 or i == (n-1)*4:
        print('*'*(mid*2+1))
    elif i == (n-1)*2:
        print('* '*mid,'*',sep='')
    elif i % 2 == 1:
        print('* '*((mid - abs(i-(mid))) // 2 + 1),' '*(abs(i-(mid))*2 -1),' *'*((mid - abs(i-(mid))) // 2 + 1),sep='')
    else:
        print('* '*((mid - abs(i-(mid))) // 2),'*'*(abs(i-(mid))*2+1),' *'*((mid - abs(i-(mid))) // 2),sep='')