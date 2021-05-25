max_health = 100
current_health = 100
bitcoins = 0
dungeon_rooms = input().split("|")
is_dead = False
room_counter = 0

for room in dungeon_rooms:
    room_counter +=1
    command = room.split(" ")

    if command[0] == 'potion': #getting health
        current_health += int(command[1])
        if current_health >= max_health:
            hp = max_health - (current_health - int(command[1]))
            current_health = 100
        else:
            hp = int(command[1])

        # if current_health + int(command[1]) >= 100:
        #     hp = 100 - current_health
        #     current_health = 100
        # else:
        #     current_health += int(command[1])
        #     hp = int(command[1])

        print(f"You healed for {hp} hp.")
        print(f"Current health: {current_health} hp.")

    elif command[0] == 'chest': #getting bitcoins
        bitcoins += int(command[1])
        print(f"You found {int(command[1])} bitcoins.")

    else: #facing monster
        current_health -= int(command[1])
        if not current_health <= 0:
            print(f"You slayed {command[0]}.")
        else:
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {current_health}")

else:
    print(f'You died! Killed by {command[0]}.')
    print(f"Best room: {room_counter}")