money = int(input('지폐로 교환할 돈은 얼마? '))
print('50000원짜리 ==>', money // 50000, '장')
money %= 50000
print('10000원짜리 ==>', money // 10000, '장')
money %= 10000
print('5000원짜리 ==>', money // 5000, '장')
money %= 5000
print('1000원짜리 ==>', money // 1000, '장')
money %= 1000
print('지폐로 바꾸지 못한 돈 :', money, '원')