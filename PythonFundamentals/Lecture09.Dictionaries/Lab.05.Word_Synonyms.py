input_nmbr = int(input())
synonyms = {}

for el in range(input_nmbr):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for k,v in synonyms.items():
    print(f'{k} - {", ".join(v)}')