#TODO MY SOLUTION
countries, capitals = input().split(', '), input().split(', ')
result = [print(f'{countries[el]} -> {capitals[el]}') for el in range(len(countries))]

# #TODO SOLUTION 2
# [print(f'{countries} -> {capitals}') for country, capital in zip(countries, capitals)]

##TODO SOLUTION 3 - AS PER TASK CONDITIONS
# my_dict = {country: capital for country, capital in zip(countries, capitals)}
# [print(f'{country} -> {capitals}') for country, capital in my_dict.items()]