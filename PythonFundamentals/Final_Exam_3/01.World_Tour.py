import re
travel_route = input()

command = input()

while not command == 'Travel':
    command = command.split(':')
    instructions = command[0]

    if instructions == 'Add Stop':
        idx = int(command[1])
        data_string = command[2]
        if 0 <= idx < len(travel_route):
            travel_route = travel_route[0:idx] + data_string + travel_route[idx:]

    elif instructions == 'Remove Stop':
        start_idx = int(command[1])
        end_idx = int(command[2])
        if 0 <= start_idx < len(travel_route) and 0 <= end_idx < len(travel_route):
            travel_route = travel_route[:start_idx] + travel_route[end_idx+1:]

    elif instructions == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in travel_route:
            travel_route = travel_route.replace(old_string, new_string, 1)
    print(travel_route)
    command = input()

print(f"Ready for world tour! Planned stops: {travel_route}")

# travel_route = re.split('::|-',travel_route)
# string_to_print = f'{travel_route[0]}::'+"-".join([travel_route[i] for i in range(1, len(travel_route))])
# a =5