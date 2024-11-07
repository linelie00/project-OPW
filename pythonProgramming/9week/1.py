age = {'Alice':25 , 'Bob': 18, 'Charlie': 30, 'David': 17}
print('20세 이상인 사람들 :', end=' ')
for name in age:
    if age[name] > 20: print(name, end=' ')
