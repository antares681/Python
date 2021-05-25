data = input()
word= ''
for i in data:
    i = (ord(i) +3) % 127
    word += chr(i)
print(word)


# ALINA
# data = input()
# words = list(data)
# encrypted_text = []
# for i in range(len(words)):
#         j = ord(words[i])
#         j += 3
#         letter = chr(j)
#         encrypted_text.append(letter)
#         letter = str(letter)