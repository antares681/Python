def char_multiplier(word_1, word_2):
    result = 0
    for i in range(len(word_1)):
        result += word_1[i] * word_2[i]
    for i in range(len(word_1), len(word_2)):
        result += word_2[i]
    return result


word_characters = []
result = []
data = input().split(' ')

for el in data:
    for ele in el:
        word_characters.append(ord(ele))
    result.append(word_characters)
    word_chars = []

if len(result[0]) <= len(result[1]):
    result_to_print = char_multiplier(result[0], result[1])
else:
    result_to_print = char_multiplier(result[1], result[0])

print(result_to_print)
