#각 단어안의 알파벳을 소문자 알파벳 순으로 정렬하여 문자열 형태로 출력
s = input("문장을 입력하세요 :")
print([''.join(sorted(i)) for i in s.split()])
