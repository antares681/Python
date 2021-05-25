# from collections import defaultdict
# text = input()
# text_to_dict = defaultdict(int)
# for el in text:
#     text_to_dict[el] += 1
#
# sorted_dict = sorted(text_to_dict.items(), key=lambda x: x[0])
# for k, v in sorted_dict:
#     print(f'{k}: {v} time/s')

from collections import defaultdict
text_to_dict = defaultdict(int)
for el in input():
   text_to_dict[el] += 1
[print(f'{k}: {v} time/s') for k, v in sorted(text_to_dict.items(), key=lambda x: x[0])]