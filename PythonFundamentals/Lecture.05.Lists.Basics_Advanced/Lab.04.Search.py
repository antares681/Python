lines_number = int(input())
key_word = input()
word_list = []
filtered_list = []

for i in range(lines_number):
    word_list.append(input())
    if key_word in word_list[i]:
        filtered_list.append(word_list[i])

print(word_list)
print(filtered_list)
