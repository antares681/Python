def string_between_two_chr(asci_start, asci_end):
    char_string = []
    for i in range (asci_start + 1, asci_end):
        char_string.append(chr(i))
    return char_string

char_1 = ord(input())
char_2 = ord(input())

result_string = string_between_two_chr(char_1,char_2)
print(' '.join(result_string))




