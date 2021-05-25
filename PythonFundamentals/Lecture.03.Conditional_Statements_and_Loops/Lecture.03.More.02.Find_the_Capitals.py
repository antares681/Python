text = input()
i = 0
capitals_list = []

for symbol in range(len(text)):
     if 64 < ord(text[symbol]) < 91 :
        capitals_list.append(symbol)
     symbol += 1
print(capitals_list)

# print(text[symbol], end="")
