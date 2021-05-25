# import re
# names = input()
# regex = "\\b[A-Z][a-z]+ +[A-Z][a-z]+\\b"
# matches = re.findall(regex, names)
# print(" ".join(matches))
#

# EXAMPLE OF FILTER SPLIT


import re
test_inputs = '1::rere-::df*dfdf::434-3434-'
test_list = re.split(r'[:\*\-]', test_inputs)
print(test_list)