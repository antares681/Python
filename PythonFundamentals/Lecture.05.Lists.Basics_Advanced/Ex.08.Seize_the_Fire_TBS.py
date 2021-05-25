# cells_list = input().split('#')
# effort = 0
# water = int(input())
# total_fire = 0
# cell_value = []
#
# for cell in cells_list:
#     cell = cell.split(" = ")
# #   print (cell)
#     type_of_fire = current_cell[0]
#     cell_value = int(current_cell[-1])
#
#     if type_of_fire  == "High":
#         if not 81 <= cell_value <= 125:
#             continue
#
#     elif type_of_fire == "Medium":
#         if not 51 <= cell_value <= 80:
#             continue
#
#     elif type_of_fire == "Low":
#         if not 1 <= cell_value <= 50:
#             continue
#
#     if water < cell_value:
#         cell_value.append(cell_value)
#         water -= cell_value
#         water += cell_value * 0.25

fire_list = input().split("#")
water = int(input())

total_effort = 0
total_fire = 0
burning_cells = []

for i in fire_list:
    cell = i.split(" = ")
    cell_value = int(cell[1])
    fire_level = cell [0]

    if fire_level == 'High' and 81 <= cell_value <= 125:
            pass

    elif fire_level == 'Medium' and 51 <= cell_value <= 80:
            pass

    elif fire_level == 'Low' and 1 <= cell_value <= 50:
            pass
    else:
        burning_cells.append(" ")
        continue

    if not water < cell_value:
        water -= cell_value
        burning_cells.append(cell_value)
    else:
        burning_cells.append(None)


print("Cells:")
print(*burning_cells, sep="\n - ")
print(f"Effort: {total_effort}")
print(f"Total Fire: {total_fire} ")