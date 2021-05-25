def decipherer(word):
    current_word = ""

    #first letter drecipher
    letter_code = [int(i) for i in word if i.isdigit()]
    letter_code_as_string = [str(i) for i in letter_code]
    ascii_code_first = "".join(letter_code_as_string)
    first_letter_symbol = chr(int(ascii_code_first))
    current_word = first_letter_symbol + word[len(ascii_code_first):]

    #second letter and last letter exchange
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    current_word = "".join(current_word)
    return current_word


cipher = input().split()

for element in cipher:
    current_word = decipherer(element)
    print(current_word, end=' ')
