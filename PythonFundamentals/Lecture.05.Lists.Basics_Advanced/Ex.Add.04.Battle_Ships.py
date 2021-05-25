def battlefield_status_check(battlefield_data):
    counter = 0
    for element in battlefield_data:
        for j in element:
            if not j == 0:
                counter += 1
    return counter

def battle_analysis(attack_commands):
    for element in attack_commands:
        ship_attack_order = [int(command) for command in element.split("-")]
        if battlefield[ship_attack_order[0]][ship_attack_order[1]] > 0:
            battlefield[ship_attack_order[0]][ship_attack_order[1]] -= 1
        else:
            battlefield[ship_attack_order[0]][ship_attack_order[1]] = 0
    return(battlefield)

#GAME PROGRAM

#Defining variables
battlefield = []
command = []

#Defining Battlefield
field_size = int(input())
for rows in range(field_size):
    battlefield.append([int(element) for element in input().split()])

#Game start
attack_commands = input().split(" ")
counter_before_battle = battlefield_status_check(battlefield)
battlefield = battle_analysis(attack_commands)
counter_after_battle = battlefield_status_check(battlefield)

#Game Results
print(counter_before_battle - counter_after_battle)

