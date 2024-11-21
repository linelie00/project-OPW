class StringUtils:
    @staticmethod
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        else: return s[::-1]
    
while(1):
    s = input('문자열을 입력하세요 : ')
    if s == 'exit':
        break
    print(StringUtils.is_palindrome(s))