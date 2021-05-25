pirate_ship_initial_status = [int(section_health) for section_health in input().split('>')]
pirate_ship_status = pirate_ship_initial_status.copy()
man_o_war_status = [int(section_health) for section_health in input().split('>')]
section_max_health = int(input())
is_game_over = False

command = input()

while not command == 'Retire':
    # WARSHIP ACTIONS
    command = command.split()

    # CHECK_1 WARSHIP -> PIRATESHIP
    if command[0] == 'Defend':
        targeted_section_start = int(command[1])
        targeted_section_end = int(command[2]) + 1
        damage = int(command[3])
        if 0 <= targeted_section_start <= len(pirate_ship_status) and 0 <= targeted_section_end <= len(pirate_ship_status):
            for targeted_section in range(targeted_section_start, targeted_section_end):
                pirate_ship_status[targeted_section] -= damage
                if pirate_ship_status[targeted_section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_game_over = True
                    break

    # PIRATESHIP ACTIONS
    # CHECK_2 PIRATESHIP -> WARSHIP
    if command[0] == 'Fire':
        targeted_section = int(command[1])
        damage = int(command[2])
        if 0 <= targeted_section <= len(pirate_ship_status):
            man_o_war_status[targeted_section] -= damage
            if targeted_section <= 0:
                print("You won! The enemy ship has sunken.")
                is_game_over = True

    # CHECK_3 PIRATESHIP
    elif command[0] == 'Repair':
        targeted_section = int(command[1])
        repair = int(command[2])
        if 0 <= targeted_section <= len(pirate_ship_status):
            pirate_ship_status[targeted_section] += repair
            if pirate_ship_status[targeted_section] > section_max_health:
                pirate_ship_status[targeted_section] = section_max_health

    # CHECK_4 PIRATESHIP
    elif command[0] == 'Status':
        quick_repair_section_list = []
        for section in range(len(pirate_ship_status)):
            if pirate_ship_status[section] < section_max_health * 0.20:
                quick_repair_section_list.append(pirate_ship_status[section])
        print(f'{len(quick_repair_section_list)} sections need repair.')

    command = input()

    if is_game_over:
        break

if not is_game_over:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(man_o_war_status)}")


#SOLUTION 2

# pirate_ship = input().split(">")
# warship = input().split(">")
# maximum_health = int(input())
# for i in range(len(pirate_ship)):
#     pirate_ship[i] = int(pirate_ship[i])
# for i in range(len(warship)):
#     warship[i] = int(warship[i])
# command = input()
# stalemate = True
# while command != "Retire":
#     command = command.split(" ")
#     if command[0] == "Fire":
#         index = int(command[1])
#         damage = int(command[2])
#         if 0 <= index < len(warship):
#             warship[index] -= damage
#             if warship[index] <= 0:
#                 stalemate = False
#                 print("You won! The enemy ship has sunken.")
#                 break
#
#     elif command[0] == "Defend":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         damage = int(command[3])
#         if 0 <= start_index < end_index < len(pirate_ship):
#             for section in range(start_index,end_index+1):
#                 pirate_ship[section] -= damage
#                 if pirate_ship[section] <= 0:
#                     stalemate = False
#                     print("You lost! The pirate ship has sunken.")
#                     break
#
#     elif command[0] == "Repair":
#         index = int(command[1])
#         health = int(command[2])
#         if 0 <= index < len(pirate_ship):
#             pirate_ship[index] += health
#             if pirate_ship[index] > maximum_health:
#                 pirate_ship[index] = maximum_health
#
#     elif command[0] == "Status":
#         counter = 0
#         for num in pirate_ship:
#             if num < maximum_health * 0.2:
#                 counter += 1
#         print(f"{counter} sections need repair.")
#
#     command = input()
# if stalemate == True:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")