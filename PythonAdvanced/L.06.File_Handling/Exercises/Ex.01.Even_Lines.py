symbols = ["-", ",", ".", "!", "?"]
final_string = []
with open('text.txt', 'r') as file:
    list_rows = file.readlines()
    filtered_lines = [list_rows[el].strip('\n') for el in range(len(list_rows)) if el % 2 == 0]
    for element in filtered_lines:
        result = []
        for symbol in range(len(element)):
            if element[symbol] in symbols:
                result.append('@')
            else:
                result.append(element[symbol])
        final_string.append(''.join(result).split())
    for el in final_string:
        print(' '.join(el[::-1]))
