#카이사르암호 해독
def decrypt_caesar(ciphertext):
    for i in range(26):
        plaintext = ''
        for c in ciphertext:
            if 'A' <= c <= 'Z':
                plaintext += chr((ord(c) - ord('A') + i) % 26 + ord('A'))
            elif 'a' <= c <= 'z':
                plaintext += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
            else:
                plaintext += c
        print(i, plaintext)
        print()
    return

if __name__ == "__main__":
    decrypt_caesar(input())