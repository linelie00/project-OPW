# 주어진 리스트에서 최대값을 찾는 재귀함수를 작성, 이 때 람다 함수를 사용
l = [23,5,2,8,1]
# max = lambda l: max(l) if len(l) == 1 else max(l[0], max(l[1:]))
max = lambda l: l[0] if len(l) == 1 else l[0] if l[0] > max(l[1:]) else max(l[1:])
print(max(l))