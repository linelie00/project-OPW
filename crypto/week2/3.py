#단일치환암호
# encryption_key = {
#     'q': 'A', 'w': 'B', 'e': 'C', 'r': 'D', 't': 'E', 'y': 'F', 'u': 'G', 'i': 'H', 'o': 'I', 'p': 'J',
#     'a': 'K', 's': 'L', 'd': 'M', 'f': 'N', 'g': 'O', 'h': 'P', 'j': 'Q', 'k': 'R', 'l': 'S', 'z': 'T',
#     'x': 'U', 'c': 'V', 'v': 'W', 'b': 'X', 'n': 'Y', 'm': 'Z'
# }

encryption_key = {
    'q': '0', 'w': '0', 'e': '0', 'r': '0', 't': '0', 'y': '0', 'u': '0', 'i': '0', 'o': '0', 'p': '0',
    'a': '0', 's': '0', 'd': '0', 'f': '0', 'g': '0', 'h': '0', 'j': '0', 'k': '0', 'l': '0', 'z': '0',
    'x': '0', 'c': '0', 'v': '0', 'b': '0', 'n': '0', 'm': '0'
}

def encrypt(text):
    cipher_text = ''
    for char in text:
        if char.lower() in encryption_key:
            cipher_text += encryption_key[char.lower()]
        else:
            cipher_text += char
    return cipher_text

plain_text = input("plain text: ")
cipher_text = encrypt(plain_text)
print("cipher text:", cipher_text)