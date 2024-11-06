import random
import string

char = string.ascii_letters + " " + string.punctuation + string.digits
chars = list(char)
key = chars.copy()

random.shuffle(key)

# print(chars)
# print(key)

# Encryption:
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("******ENCRYPTION******")
print(f"Original Message: {plain_text}")
print(f"Encryted Message: {cipher_text}")

# Decryption:
encrypted_text = input("Enter the encrypted message: ")
decrypted_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    decrypted_text += chars[index]

print("******DECRYPTION******")
print(f"Orginal Message : {decrypted_text}")