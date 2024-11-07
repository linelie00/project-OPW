#주어진 딕셔너리에서 값이 리스트인 경우
# 리스트의 길이를 값으로 하는 새로운 딕셔너리를 만드시오.

data = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9], 'd':10}
new_data = {}
for key in data:
    if type(data[key]) == list:
        new_data[key] = len(data[key])
    else:
        new_data[key] = data[key]

print(new_data)