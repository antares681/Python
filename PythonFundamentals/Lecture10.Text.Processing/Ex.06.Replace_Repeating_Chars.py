data_string = input()
string_to_print = []

for char in data_string:
    if len(string_to_print) > 0:
        if not char == string_to_print[-1]:
            string_to_print.append(char)
    else:
        string_to_print.append(char)
print("".join(string_to_print))

