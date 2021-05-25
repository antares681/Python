import re
text = input(

valid_sited = [el.group() for el in re.finditer(pattern, text)]
    if valid_sites:
        valids.extend(vaild_sites)

    text=input()

print(*valids, sep='\n')