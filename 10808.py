s = [ord(c) for c in input()]
for i in range(ord('a'),ord('z')+1):
    print(s.count(i), end=' ')