l = [1,2,3]
t = (4,5,6)
l.reverse()
t = tuple(l) + t[0:3:2]
print(t)