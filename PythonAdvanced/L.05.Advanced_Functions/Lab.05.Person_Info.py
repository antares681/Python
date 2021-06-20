#TODO SOLUTION 1

# def get_info(name, age, town):
#     return f'This is {name} from {town} and he is {age} years old'
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

#TODO SOLUTION 2
#
# get_info = lambda name, town, age: f'This is {name} from {town} and he is {age} years old'
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


#TODO SOLUTION 3
def get_info(**kwargs):
    return f'This is {"name"} from {"town"} and he is {"age"} years old'

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_info(name = "George", town = "Sofia", age = 20))