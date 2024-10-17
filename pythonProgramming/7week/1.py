list1 = [1,2,3]
list2 = [3,4,5]
list1 = list1 + list2
print("1st", list1)
print("2의 인덱스 :", list1.index(2))
list1.remove(1)
print("3의 개수 :", list1.count(3))
print("최대값-최소값 :", max(list1) - min(list1))