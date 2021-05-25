my_list = input().split("|")
command = input()

while not command == "Shop!":
    if "Important" in command:
        task = command.split("%")
        item = task[1]
        if item in my_list:
            my_list.remove(item)
            my_list.insert(0, item)

    elif "Add" in command:
        task = command.split("%")
        item = task[1]
        if item not in my_list:
            my_list.append(item)
        else:
            print("The product is already in the list.")

    elif "Swap" in command:
        task = command.split("%")
        prod_1 = task[1]
        prod_2 = task[2]

        if prod_1 in my_list and prod_2 in my_list:
            a, b = my_list.index(prod_1), my_list.index(prod_2)
            my_list[a], my_list[b] = my_list[b], my_list[a]
        else:
            if prod_1 not in my_list:
                print(f"Product {prod_1} missing!")
            if prod_2 not in my_list:
                print(f"Product {prod_2} missing!")

    elif "Remove" in command:
        task = command.split("%")
        item = task[1]
        if item in my_list:
            my_list.remove(item)
        else:
            print(f"Product {item} isn't in the list.")
    command = input()

for i, item in enumerate(my_list, 1):
    print(i, ". " + item, sep="")