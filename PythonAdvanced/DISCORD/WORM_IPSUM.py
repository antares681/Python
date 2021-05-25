# #TODO REGEX SOLUTION 50%

# import re
# pattern = re.compile(r'(^[A-Z][A-Za-z\s]+[\.\?\!]$)')
#
# most_occurring_symbol = ""
# mos_counter = 1  #Most Occurring Symbol (mos) counter
# curr_word = ""
# final = []
#
# data = input()
#
# while not data == "Worm Ipsum":
#     is_valid = pattern.match(data)
#     if is_valid:
#         list_of_words = data.split(" ")
#         #ITERRATING OVER WORDS & SYMBOLS IN WORDS
#         for word in list_of_words:
#             for symbol in word:
#                 symbol_count = word.count(symbol)
#                 if symbol_count > mos_counter:
#                     most_occurring_symbol = symbol
#                     mos_counter = symbol_count
#
#             if not most_occurring_symbol == "":
#                 if word[-1] == ".":
#                     curr_word = (len(word)-1) * most_occurring_symbol + word[-1]
#                 else:
#                     curr_word = len(word) * most_occurring_symbol
#                 final.append(curr_word)
#             else:
#                 final.append(word)
#             #RESET COUNTER & MOS SYMBOL
#             most_occurring_symbol = ""
#             mos_counter = 1
#         print(' '.join(final))
#         #RESET LIST FOR NEXT WORD
#         final = []
#     data = input()


# #TODO NO REGEX SOLUTION 80%

# dot = "."
# is_valid = False
# most_occurring_symbol = ""
# mos_counter = 1  #Most Occurring Symbol (mos) counter
# curr_word = ""
# final = []
#
# data = input()
#
# while not data == "Worm Ipsum":
#     if data.count(dot) == 1 and data[-1] == dot and data[0].isupper():
#         is_valid = True
#
#     if is_valid:
#         list_of_words = data.split(" ")
#         #ITERRATING OVER WORDS & SYMBOLS IN WORDS
#         for word in list_of_words:
#             for symbol in word:
#                 symbol_count = word.count(symbol)
#                 if symbol_count > mos_counter:
#                     most_occurring_symbol = symbol
#                     mos_counter = symbol_count
#
#             if not most_occurring_symbol == "":
#                 if word[-1] == dot:
#                     curr_word = (len(word)-1) * most_occurring_symbol + word[-1]
#                 else:
#                     curr_word = len(word) * most_occurring_symbol
#                 final.append(curr_word)
#             else:
#                 final.append(word)
#             #RESET COUNTER & MOS SYMBOL
#             most_occurring_symbol = ""
#             mos_counter = 1
#         print(' '.join(final))
#         #RESET LIST FOR NEXT WORD
#         final = []
#         is_valid = False
#     data = input()




# #TODO REGEX 50%
# import re
# pattern = re.compile(r'(^[A-Z][A-Za-z\s]+[\.\?\!]$)')
# most_occurring_letter = ""
# mol_counter = 1  #Most Occurring Letter (mos) counter
# curr_word = ""
# final = []
# data = input()
#
# while not data == "Worm Ipsum":
#     is_valid = pattern.match(data)
#     if is_valid:
#         list_of_words = data.split(" ")
#
#         for word in list_of_words:
#             letters_count = {letter: word.count(letter) for letter in word}
#             most_occurring_letter, mol_counter = max(letters_count, key=letters_count.get), int(sorted(letters_count.items(), key = lambda x: -x[1])[0][1])
#             if mol_counter > 1:
#                 if word[-1] == ".":
#                     curr_word = (len(word)-1) * most_occurring_letter + word[-1]
#                 else:
#                     curr_word = len(word) * most_occurring_letter
#                 final.append(curr_word)
#             else:
#                 final.append(word)
#             continue
#
#         print(*final, sep=' ')
#         #RESET LIST BEFORE NEXT WORD LOOP
#         final = []
#     data = input()

#NON-REGEX 80%
dot = "."
is_valid = False
most_occurring_letter = ""
mol_counter = 1  #Most Occurring Letter (mos) counter
curr_word = ""
final = []
data = input()

while not data == "Worm Ipsum":
    if data.count(dot) == 1 and data[-1] == dot and data[0].isupper():
        is_valid = True

    if is_valid:
        list_of_words = data.split(" ")

        for word in list_of_words:
            letters_count = {letter: word.count(letter) for letter in word}
            most_occurring_letter, mol_counter = max(letters_count, key=letters_count.get), int(sorted(letters_count.items(), key = lambda x: -x[1])[0][1])
            if mol_counter > 1:
                if word[-1] == ".":
                    curr_word = (len(word)-1) * most_occurring_letter + word[-1]
                else:
                    curr_word = len(word) * most_occurring_letter
                final.append(curr_word)
            else:
                final.append(word)

        print(*final, sep=' ')
        #RESET LIST BEFORE NEXT WORD LOOP
        final = []
        is_valid = False
    data = input()