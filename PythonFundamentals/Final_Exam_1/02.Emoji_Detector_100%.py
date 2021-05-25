import re
data = input()
cool_threshold = 1
pattern_threshold = re.compile(r'\d')
smiley_counter = []
for i in pattern_threshold.findall(data):
    cool_threshold *= int(i)
print(f'Cool threshold: {cool_threshold}')

pattern = re.compile(r'(\:\:)([A-Z][a-z]{2,})(\:\:)|(\*\*)([A-Z][a-z]{2,})(\*\*)')

cool_emojis = []
for match in pattern.finditer(data):
    smiley = match.group()
    if not smiley in smiley_counter:
        smiley_counter.append(smiley)
    smiley_threshold = 0
    for symbol in smiley:
        if not symbol == ':' and not symbol == '*':
            smiley_threshold += ord(symbol)
    if smiley_threshold >= cool_threshold:
        cool_emojis.append((match.group()))
print(f'{len(smiley_counter)} emojis found in the text. The cool ones are:')
cool_emojis = [i for i in cool_emojis]
print('\n'.join(cool_emojis))