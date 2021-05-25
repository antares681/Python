decryption_key = int(input())
lines_number = int(input())
decrypted_string = ""

for i in range(0, lines_number):
    encrypted_symbol = input()
    decrypted_string += chr(ord(encrypted_symbol)+decryption_key)

print(decrypted_string)

