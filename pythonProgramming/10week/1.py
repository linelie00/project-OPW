s = input()
print('거꾸로 출력 :', s[::-1])
print('공백 제거 :', s.replace(' ', ''))
print('첫/마지막 글자 대문자 :', s[0].upper() + s[1:-1] + s[-1].upper())