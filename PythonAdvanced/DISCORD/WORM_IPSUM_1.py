line = input()

while not line == "Worm Ipsum":

    valid = False
    if line.count('.') == 1:
        valid = True
        if valid:
            list_words = line.split()
            final = []
            for word in list_words:
                modded_word = word
                chars_dict = {}
                for char in word:
                    if char not in chars_dict:
                        chars_dict[char] = 0
                    chars_dict[char] += 1
                most_oc = max(chars_dict, key= chars_dict.get)
                occurence = max(chars_dict.values())
                if occurence > 1:
                    if word[-1] == ".":
                        modded_word = most_oc * len(word[:-1])+"."
                    else:
                        modded_word = most_oc*len(word)
                final.append(modded_word)
            print(' '.join(final))

    line = input()