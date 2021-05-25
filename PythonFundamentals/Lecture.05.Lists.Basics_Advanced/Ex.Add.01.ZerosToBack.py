# nums = input().split(", ")
# upd_nums = []
# zero_list = []
#
# for i in nums:
#     if not i == "0":
#         upd_nums.append(i)
#     else:
#         zero_list.append("0")
#
# print(f'[{", ".join(upd_nums + zero_list)}]')


# OPTIMAL SOLUTION
nums = input().split(", ")
upd_nums = []
zero_list = []

for i in nums:
    i = int(i) + 5
    if not i == 0:
        upd_nums.append(i)
    else:
        zero_list.append(0)
print(upd_nums + zero_list) #!!!!!!!! MOST IMPORTANT

