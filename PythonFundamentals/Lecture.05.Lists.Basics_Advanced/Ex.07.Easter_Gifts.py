#60/100

gifts_list = input().split(" ")

while True:
    updated_gifts_list = []

    command = input()

    if command == "No Money":
        break
    else:
        command_elements = command.split()

        if command_elements[0] == "OutOfStock":
            for item in gifts_list:
                if item == command_elements[1]:
                    updated_gifts_list.append("None")
                else:
                    updated_gifts_list.append(item)
                gifts_list = updated_gifts_list

        elif command_elements[0] == "Required":
            if 0 < int(command_elements[2]) < len(gifts_list):
                gifts_list[int(command_elements[2])] = command_elements[1]

        elif command_elements[0] == "JustInCase":
           gifts_list[-1] = command_elements[1]

while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep=" ")