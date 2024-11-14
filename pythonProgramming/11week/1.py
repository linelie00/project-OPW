# 자음만 출력
s = "Python programming is fun!"
for i in s:
    if i in 'aeiouAEIOU':
        continue
    print(i, end='')
print()