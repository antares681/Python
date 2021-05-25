def todo_list_creator (command):
    todo_list = [0] * 10

    while not command == "End":
        importance, task = command.split("-")
        importance = int(importance) - 1
        todo_list[importance] = task
        command = input()
    return todo_list

task = input()

print([task for task in todo_list_creator(task) if not task == 0])