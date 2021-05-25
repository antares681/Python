def text_reader(data_file):
    symbols = ["-", ",", ".", "!", "?", "'"]
    line_nmbr = 0
    with open(data_file, 'r') as file:
        data = file.readlines()
        for el in data:
            line_nmbr += 1
            el = el.strip('\n')
            letters, punctuation_marks  = 0, 0
            for symbol in el:
                if symbol in symbols:
                    punctuation_marks +=1
                elif symbol not in symbols and not symbol == ' ':
                    letters += 1
            text_writer(el, letters, punctuation_marks, line_nmbr)

def text_writer(el, lt, pm, ln):
    with open('output.txt', 'a') as file:
        file.write(f'Line {ln}: {el} ({lt})({pm})\n')

text_reader('text.txt')