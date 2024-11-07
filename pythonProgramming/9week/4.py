#문자열 입력받고 각 문자 출현 횟수 딕셔너리로 출력

s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)