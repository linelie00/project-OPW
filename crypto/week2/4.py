from collections import Counter

# 단일치환암호 키
# encryption_key = {
#     'q': 'A', 'w': 'B', 'e': 'C', 'r': 'D', 't': 'E', 'y': 'F', 'u': 'G', 'i': 'E', 'o': 'I', 'p': 'J',
#     'a': 'K', 's': 'L', 'd': 'M', 'f': 'N', 'g': 'O', 'h': 'P', 'j': 'H', 'k': 'R', 'l': 'S', 'z': 'T',
#     'x': 'U', 'c': 'V', 'v': 'W', 'b': 'X', 'n': 'Y', 'm': 'Z'
# }

encryption_key = {
    'q': '0', 'w': '0', 'e': '0', 'r': '0', 't': '0', 'y': '0', 'u': '0', 'i': 'A', 'o': '0', 'p': '0',
    'a': '0', 's': '0', 'd': 'N', 'f': '0', 'g': 'H', 'h': '0', 'j': 'I', 'k': '0', 'l': '0', 'z': '0',
    'x': '0', 'c': '0', 'v': '0', 'b': 'T', 'n': '0', 'm': 'E'
}

# 암호화 함수
def encrypt(text):
    cipher_text = ''
    for char in text:
        if char.lower() in encryption_key:
            cipher_text += encryption_key[char.lower()]
        else:
            cipher_text += char
    return cipher_text

# 빈도수 계산 함수 (입력값 기준)
def count_frequency(text):
    filtered = [c.lower() for c in text if c.isalpha()]
    return Counter(filtered)

# 실행부
plain_text = input("plain text: ")

# 평문 알파벳 빈도수
freq_plain = count_frequency(plain_text)
print("\n[입력값 알파벳 빈도수]")
for letter, count in sorted(freq_plain.items()):
    print(f"{letter}: {count}")

# 암호화
cipher_text = encrypt(plain_text)
print("\n[cipher text]:", cipher_text)
