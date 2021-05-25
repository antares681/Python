num = []  #num = list()

############ ПЕРИМЕР НА ЛИСТ

# tail = input()
# body = input()
# head = input()
#
# zoo = [head, body, tail]
#
# print(zoo)

############ Метод при листове

some_text = "a  b c d"
print(some_text)
result = some_text.split(" ") #по подразбиране е сплит по празни места
result.append("e")
print(result)

back_to_string = "-".join(result)
print(back_to_string)

########## ПРИНТИРАНЕ НА ЛИСТОВЕ
# nums = [1,2,3]
#
# for nums in (1,2,3):
#     print(nums)
#
# for index in range(0, len(nums)):
#     print(nums[])