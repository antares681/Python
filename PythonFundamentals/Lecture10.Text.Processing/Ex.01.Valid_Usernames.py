data = input().split(', ')
is_valid = True
word = []
selection =[]

for el in data:
    if 3 < len(el) < 16:
        word.append(el)
        word[0].replace('-', "")
        if '-' in word[0]:
            word[0] = word[0].replace('-', "")
        if word[0].isidentifier():
            selection.append(el)
        word = []

print("\n".join(selection))

