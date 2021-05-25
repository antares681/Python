# def house_status_checker(status, neighborhood_current):
#     result = ''
#     if neighborhood_current[status] > 0:
#             result = f"Place {status} has Valentine's day."
#     else:
#         result = f"Place {status} already had Valentine's day."
#
#     return result, neighborhood_current
#
# neighborhood = [int(house) for house in input().split('@')]
# current_location_index = 0
# neighborhood_size = len(neighborhood)
#
# while True:
#     command = input().split(" ")
#     if command[0] == "Love!":
#         break
#
#     if command[0] == "Jump":
#         jump_length = int(command[1])
#
#         current_location_index += jump_length
#         if 0 <= current_location_index < neighborhood_size:
#             if neighborhood[current_location_index] > 0:
#                 neighborhood[current_location_index] -= 2
#                 if neighborhood[current_location_index] == 0:
#                     print(f"Place {current_location_index} has Valentine's day.")
#             else:
#                 print(f"Place {current_location_index} already had Valentine's day.")
#         else:
#             current_location_index = 0
#             if neighborhood[current_location_index] > 0:
#                 neighborhood[current_location_index] -= 2
#                 if neighborhood[current_location_index] == 0:
#                     print(f"Place {current_location_index} has Valentine's day.")
#             else:
#                 print(f"Place {current_location_index} already had Valentine's day.")
#
# print(f"Cupid's last position was {current_location_index}.")
#
# if not sum(neighborhood) == 0:
#     print(f'Cupid has failed {neighborhood_size - neighborhood.count(0)} places.')
#
# else:
#     print(f'Mission was successful.')

#SOLUTION 2

neighborhood = [int(house) for house in input().split('@')]
current_location_index = 0
neighborhood_size = len(neighborhood)

while True:
    command = input().split(" ")
    if command[0] == "Love!":
        break
    if command[0] == "Jump":
        jump_length = int(command[1])

        current_location_index += jump_length
        if 0 <= current_location_index < neighborhood_size:
            if neighborhood[current_location_index] > 0:
                neighborhood[current_location_index] -= 2
                if neighborhood[current_location_index] == 0:
                    print(f"Place {current_location_index} has Valentine's day.")
            else:
                print(f"Place {current_location_index} already had Valentine's day.")
        else:
            current_location_index = 0
            if neighborhood[current_location_index] > 0:
                neighborhood[current_location_index] -= 2
                if neighborhood[current_location_index] == 0:
                    print(f"Place {current_location_index} has Valentine's day.")
            else:
                print(f"Place {current_location_index} already had Valentine's day.")

print(f"Cupid's last position was {current_location_index}.")

if not sum(neighborhood) == 0:
    print(f'Cupid has failed {neighborhood_size - neighborhood.count(0)} places.')

else:
    print(f'Mission was successful.')

#SOLUTION 3
#з
# houses_hearts = [int(el) for el in input().split("@")]
# command = input()
# index_to_jump = 0
# while not command == "Love!":
#     jump = command.split()[1]
#     index_to_jump += jump
#     if index_to_jump >= len(houses_hearts):
#         index_to_jump = 0
#     if houses_hearts[index_to_jump] != 0:
#         houses_hearts[index_to_jump] -= 2
#         if houses_hearts[index_to_jump] == 0:
#             print(f"Place {index_to_jump} has Valentine's day.")
#     else:
#         print(f"Place {index_to_jump} already had Valentine's day.")
#     command = input()
# print(f"Cupid's last position was {index_to_jump}.")
# print("Mission was successful." if sum(houses_hearts) == 0 else f"Cupid has failed {len([x for x in houses_hearts if x != 0])} places.")