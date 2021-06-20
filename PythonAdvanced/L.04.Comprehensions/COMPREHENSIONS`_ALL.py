#DICTIONARY COMPREHENSION
nums = [1, 2, 3]
cubes = {num:num **3 for num in nums }

#TODO  SET COMPREHENSION
nums = [1, 2, 3, 1, 3, 4]
unique = {num for num in nums} # a = set()

print(ord('a'))
print(chr(97))

#TODO  NESTED COMPREHENSION

[[j for j in range(2)] for i in range(4)]