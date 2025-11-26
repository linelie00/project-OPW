s = [ord(c) for c in input()]
for i in range(ord('a'),ord('z')+1):
    if i in s:
        print(s.index(i),end=" ")
    else:
        print('-1',end=" ")