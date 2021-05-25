parking_database = {}
input_nmbr = int(input())

for i in range (input_nmbr):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == 'register' and username in parking_database:
        license_plate = command[2]
        print(f"ERROR: already registered with plate number {parking_database[username]}")

    elif action == 'register' and username not in parking_database:
        license_plate = command[2]
        parking_database[username] = license_plate
        print(f"{username} registered {license_plate} successfully")

    if action == 'unregister' and username not in parking_database:
        print(f"ERROR: user {username} not found")

    elif action == 'unregister' and username in parking_database:
        print(f"{username} unregistered successfully")
        parking_database.pop(username)
for k, v in parking_database.items():
    print(f'{k} => {v}')


