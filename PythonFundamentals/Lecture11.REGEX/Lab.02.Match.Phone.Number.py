# Soltion XX
import re
print(', '.join([str(nmbr) for nmbr in [nmbr for el in re.findall(r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)', input()) for nmbr in el if '+359' in nmbr]]))

# #Solution 00
# import re
# matches = re.findall(r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)', input())
# print(', '.join([str(nmbr) for nmbr in [nmbr for el in matches for nmbr in el if '+359' in nmbr]]))

# # Solution 01
# import re
# matches = re.findall(r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)', input())
# nmbrs_to_print = [nmbr for el in matches for nmbr in el if '+359' in nmbr]
# print(', '.join([str(nmbr) for nmbr in nmbrs_to_print]))
#
#
# # Solution 02
# import re
# test_string = input()
# pattern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)'
# matches = re.findall(pattern, test_string)
# nmbrs_to_print = [nmbr for el in matches for nmbr in el if '+359' in nmbr]
# print(', '.join([str(nmbr) for nmbr in nmbrs_to_print]))
#
#
#Solution 03
# import re
# test_string = input()
# pattern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)'
# matches = re.findall(pattern, test_string)
#
# nmbrs_to_print =[]
# for el in matches:
#     for nmbr in el:
#         if '+359' in nmbr:
#             nmbrs_to_print.append(nmbr)
# print(', '.join([str(nmbr) for nmbr in nmbrs_to_print]))
# # # '+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222'
#
# \+359( |-)2( |-){\d3}