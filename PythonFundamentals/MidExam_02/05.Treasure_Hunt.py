# initial_loot = input().split("|")
#
# command = input()
#
# while not command == "Yohoho!":
#     command = command.split(" ")
#
# #Check1
#     if command[0] == 'Loot':
#         for item in command[1:]:
#             if item not in initial_loot:
#                 initial_loot.insert(0, item)
# #Check2
#     elif command[0] == 'Drop':
#         index = int(command[1])
#         #if 0 <= index < len(initial_loot):
#         #if index >= 0 and index < len(initial_loot):
#         if index in range(len(initial_loot)):
#             initial_loot.append(initial_loot.pop(index))
#
# #Check3
#     elif command[0] == 'Steal':
#         stolen_items = []
#         index = int(command[1])
#         initial_loot = initial_loot[::-1]
#
#         #CHECK TREASURE AND QTY OF ITEMS TO BE STOLEN
#         if 0 <= index <= len(initial_loot):
#             index = index
#         elif index > len(initial_loot):
#             index = len(initial_loot)
#         else:
#             index = 0
#
#         for item in range(index):
#             stolen_items.append(initial_loot.pop(0))
#
#         print(', '.join(reversed(stolen_items)))
#         initial_loot = initial_loot[::-1]
#
#     command = input()
#
# if initial_loot:
#     average_gain = 0
#     for item in initial_loot:
#         average_gain += len(item)
#     average_gain /= len(initial_loot)
#     print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
# else:
#     print(f"Failed treasure hunt.")

# #SOLUTION 2
#
# initial_loot = input().split("|")
# command = input()
# while not command == "Yohoho!":
#
#     command = command.split(" ")
#     if command[0] == 'Loot':
#         for item in command[1:]:
#             if item not in initial_loot:
#                 initial_loot.insert(0, item)
#
#     elif command[0] == 'Drop':
#         index = int(command[1])
#         if 0 <= index < len(initial_loot):
#             initial_loot.append(initial_loot.pop(index))
#
#
#     elif command[0] == 'Steal':
#         index = int(command[1])
#         if index >= len(initial_loot):
#             print(', '.join(initial_loot))
#             initial_loot = []
#         else:
#             stolen = []
#             for i in range(index):
#                 stolen.append(initial_loot.pop())
#             print(', '.join(stolen[::-1]))
#
#
#     command = input()
#
#
# if initial_loot:
#     average_gain = 0
#     for item in initial_loot:
#         average_gain += len(item)
#     average_gain /= len(initial_loot)
#     print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
# else:
#     print(f"Failed treasure hunt.")

#SOLUTION 3

initial_loot = input().split("|")
command = input()

while not command == "Yohoho!":
    command = command.split(" ")
#Check1
    if command[0] == 'Loot':
        for item in command[1:]:
            if item not in initial_loot:
                initial_loot.insert(0, item)
#Check2
    elif command[0] == 'Drop':
        index = int(command[1])
        if index in range(len(initial_loot)):
            initial_loot.append(initial_loot.pop(index))
#Check3
    elif command[0] == 'Steal':
        stolen_items = []
        index = int(command[1])
    #CHECK TREASURE AND QTY OF ITEMS TO BE STOLEN
        if 0 <= index <= len(initial_loot):
            pass
        elif index > len(initial_loot):
            index = len(initial_loot)
        for item in range(index):
            stolen_items.append(initial_loot.pop())
        print(', '.join(reversed(stolen_items)))
    command = input()
#AVERAGE GAIN CALCULATOR
if initial_loot:
    average_gain = 0
    for item in initial_loot:
        average_gain += len(item)
    average_gain /= len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
