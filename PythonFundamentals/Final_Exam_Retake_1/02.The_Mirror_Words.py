import re
regex = re.compile(r'(?P<selector>([@#]))(?P<word_1>[A-Za-z]{3,})\1\1(?P<word_2>[A-Za-z]{3,})\1')
mirror_words = {}
matches_list =[]
data = input()

for match in regex.finditer(data):
    matches_list.append(match.group())
    word_1_symbols, word_2_symbols = [ord(i) for i in match['word_1']], [ord(i) for i in match['word_2']]

    if word_1_symbols[::-1] == word_2_symbols:
        mirror_words[(match['word_1'])] = match['word_2']

if len(matches_list) == 0:
    print(f"No word pairs found!")
else:
    print(f'{len(matches_list)} word pairs found!')

if len(mirror_words) == 0:
    print(f'No mirror words!')
else:
    print(f'The mirror words are:')
    result_to_print = ', '.join([f'{k} <=> {v}' for k, v in mirror_words.items()])
    print(result_to_print)