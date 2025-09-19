import secrets

secure_number = secrets.randbelow(100)
print(secure_number)

secure_token = secrets.token_hex(16)
print(secure_token)
