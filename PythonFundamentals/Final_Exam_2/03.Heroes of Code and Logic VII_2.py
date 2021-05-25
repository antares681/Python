def hpChecker(hp):
    if hp > max_hp:
        return max_hp
    return hp

def mpChecker(mp):
    if mp > max_mp:
        return max_mp
    return mp

nmbr_of_heroes = input()
max_hp = 100
max_mp = 200
party = {}

for hero in range(int(nmbr_of_heroes)):
    hero_name, hp, mp = input().split(' ')
    party[hero_name] = [int(hp), int(mp)]

command = input()
while not command == 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        hero_name, mp, spell_name = command[1], int(command[2]), command[3]
        if party[hero_name][1] >= mp:
            party[hero_name][1] =  party[hero_name][1]- mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {party[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        if party[hero_name][0] > damage:
            party[hero_name][0] -= damage
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {party[hero_name][0]} HP left!')
        else:
            print(f'{hero_name} has been killed by {attacker}!')
            party.pop(hero_name)

    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        current_mp = party[hero_name][1] * 1
        party[hero_name][1] += amount
        party[hero_name][1] = mpChecker(party[hero_name][1])
        print(f"{hero_name} recharged for {party[hero_name][1] - current_mp} MP!")

    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        current_hp = party[hero_name][0] * 1
        party[hero_name][0] += amount
        party[hero_name][0] = hpChecker(party[hero_name][0])
        print(f"{hero_name} healed for {party[hero_name][0] - current_hp} HP!")
    command = input()

for item1, item2 in sorted(party.items(), key= lambda x: (-x[1][0], x[0])):
    print(f'{item1}\n  HP: {item2[0]}\n  MP: {item2[1]}')