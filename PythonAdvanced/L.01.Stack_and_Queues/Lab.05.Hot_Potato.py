def solve():
    kids_list = input().split()
    step = int(input())
    position = 0
    while len(kids_list) > 1:
        step -= 1
        position = (position + step) % len(kids_list)
        print(f'Removed {kids_list.pop(position)}')
        step += 1
    print(f'Last is {kids_list.pop(0)}')
#
# solve()

#TODO КОЕ МУ Е ОПАШКАТА НА ТАЗИ ЗАДАЧА, КАТО ТУК НЯМА ПЪРВИ ВЛЯЗЪЛ ПЪРВИ ИЗЛИЗА? Горе 0.050. долу 0.080

from collections import deque

def solve():
    kids_list = deque(input().split())
    toss_counter = 0
    idx = int(input())-1
    while len(kids_list) > 1:
        if not toss_counter == idx:
            kids_list.append(kids_list.popleft())
            toss_counter+=1
        else:
            print(f"Removed {kids_list.popleft()}")
            toss_counter = 0
    print(f"Last is {kids_list.popleft()}")

solve()