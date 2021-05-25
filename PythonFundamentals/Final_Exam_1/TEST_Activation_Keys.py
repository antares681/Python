text = input()
command = input()

while not command == "Generate":
    command = command.split(">>>")
    todo = command[0]
    if command[0] == "Contains":
        if command[1] in text:
            print(f"{command[1]} contains {text}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start, end = int(command[2]), int(command[3])
        if command[1] == "Upper":
            text = text[:start] + text[start:end].upper() + text[end:]
        elif command[1] == "Lower":
            text = text[:start] + text[start:end].lower() + text[end:]
        print(text)
    elif command[0] == 'Slice':
        start_slice, end_slice = int(command[1]), int(command[2])
        text = text[:start_slice] + text[end_slice:]
        print(text)
    command = input()
print(f"Your activation key is: {text}")