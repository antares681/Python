our_dict = {}
n = int(input())
for _ in range(n):
    name, h, m = input().split()
    our_dict[name] = [int(h), int(m)]
command = input()
while command != 'End':
    command = command.split(' - ')
    if len(command) == 3:
        _, hero_name, amount = command
        amount = int(amount)
        if _ == 'Recharge':
            if our_dict[hero_name][1] + amount > 200:
                gain = 200 - our_dict[hero_name][1]
            else:
                gain = amount
            print(f"{hero_name} recharged for {gain} MP!")
            our_dict[hero_name][1] += gain
        elif _ == 'Heal':
            if our_dict[hero_name][0] + amount > 100:
                gain = 100 - our_dict[hero_name][0]
            else:
                gain = amount
            print(f"{hero_name} healed for {gain} HP!")
            our_dict[hero_name][0] += gain
    elif len(command) == 4:
        _, hero_name, dmg_or_mana, spell_or_attacker = command
        if _ == 'CastSpell':
            mana = int(dmg_or_mana)
            spell = spell_or_attacker
            if our_dict[hero_name][1] >= mana:
                print(f"{hero_name} has successfully cast {spell} and now has {our_dict[hero_name][1] - mana} MP!")
                our_dict[hero_name][1] -= mana
            else:
                print(f"{hero_name} does not have enough MP to cast {spell}!")
        elif _ == 'TakeDamage':
            dmg = int(dmg_or_mana)
            attacker = spell_or_attacker
            if dmg >= our_dict[hero_name][0]:
                print(f"{hero_name} has been killed by {attacker}!")
                our_dict.pop(hero_name)
            else:
                print(
                    f"{hero_name} was hit for {dmg} HP by {attacker} and now has {our_dict[hero_name][0] - dmg} HP left!")
                our_dict[hero_name][0] -= dmg

    command = input()

for key, value in sorted(our_dict.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{key}\n  HP: {value[0]}\n  MP: {value[1]}')