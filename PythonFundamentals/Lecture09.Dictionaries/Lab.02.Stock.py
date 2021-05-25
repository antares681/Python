# data = input().split()
# products = {}
#
# for index in range(0, len(data), 2):
#     current_product = data[index]
#     quantity = int(data[index + 1])
#     products[current_product] = quantity
#
# print(products)

products_dict = {}
products_list = input().split()
search_list = input().split()
print(products_list)

for element in range(0, len(products_list), 2):
    dict_keys = products_list[element]
    dict_values = products_list[element+1]
    products_dict[dict_keys] = dict_values

for el in search_list:
        if el in products_dict:
            print(f"We have { } of {el} left")
        else:
            print(f"Sorry, we don't have {el}")
