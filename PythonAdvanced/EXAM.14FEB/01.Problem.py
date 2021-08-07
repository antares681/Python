from collections import deque

def check_fireworks(fireworks):
    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 and fireworks['Crossette Fireworks'] >= 3:
        print("Congrats! You made the perfect firework show!")
    else:
        print("Sorry. You can't make the perfect firework show.")

def check_left(fireworks_eff, explosive_power):
    if len(fireworks_eff) > 0:
        print(f"Firework Effects left: {', '.join(map(str, fireworks_eff))}")
    if len(explosive_power) > 0:
        print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

def solve(fireworks_eff, explosive_power, fireworks):
    mix = fireworks_eff[0]+ explosive_power[-1]

    if mix % 3 == 0 and mix % 5 == 0:
        processor(fireworks_eff, explosive_power)
        fireworks['Crossette Fireworks'] += 1
        return fireworks
    elif mix % 5 == 0:
        processor(fireworks_eff, explosive_power)
        fireworks['Willow Fireworks'] += 1
        return fireworks
    elif mix % 3 == 0:
        processor(fireworks_eff, explosive_power)
        fireworks['Palm Fireworks'] += 1
        return fireworks
    else:
        if fireworks_eff[0]-1 > 0:
            return fireworks_eff.append(fireworks_eff.popleft()-1)
        return fireworks_eff.popleft()

def processor(fireworks_eff, explosive_power):
    fireworks_eff.popleft()
    explosive_power.pop()
    return

fireworks_eff = deque([x for x in map(int, input().split(', ')) if x > 0])
explosive_power = deque([x for x in map(int, input().split(', ')) if x > 0])
fireworks = {'Palm Fireworks' : 0, 'Willow Fireworks' : 0, 'Crossette Fireworks' : 0}

#TODO SOLVE PROBLEM

while fireworks_eff and explosive_power:
    solve(fireworks_eff, explosive_power, fireworks)
check_fireworks(fireworks)
check_left(fireworks_eff, explosive_power)
[print(f'{k}: {v}') for k, v in fireworks.items()]




#TODO TEST INPUTS

# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
