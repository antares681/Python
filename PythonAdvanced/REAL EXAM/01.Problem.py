from collections import deque

def get_ingradients():
    chocolates = deque([x for x in map(int, input().split(', '))])
    cups_of_milk = deque([x for x in map(int, input().split(', ')) if x >= 0])
    return chocolates, cups_of_milk

def check_shakes(chocolates, cups, shakes_counter):
    if len(cups) > 0 and len(chocolates) > 0:
        if not chocolates[-1] <= 0:
            if cups[0] == chocolates[-1]:
                cups.popleft()
                chocolates.pop()
                shakes_counter['shakes'] +=1
                return chocolates, cups, shakes_counter
            else:
                chocolates[-1] -= 5
                cups.append(cups.popleft())
                return chocolates, cups, shakes_counter
        else:
            chocolates.pop()
    return chocolates, cups, shakes_counter

def check_left(chocolates, cups):
    if len(chocolates) > 0:
        print(f"Chocolate: {', '.join(map(str, chocolates))}")
    else:
        print("Chocolate: empty")
    if len(cups) > 0:
        print(f"Milk: {', '.join(map(str, cups))}")
    else:
        print("Milk: empty")


shakes_counter = {'shakes':0}
chocolates, cups_of_milk = get_ingradients()
is_done = False

while True:
    chocolates, cups, shakes_counter = check_shakes(chocolates, cups_of_milk, shakes_counter)
    if shakes_counter['shakes'] >= 5:
        is_done = True
        break
    if len(cups_of_milk) <= 0:
        break
    if len(chocolates) <= 0:
        break

#FIRST LINE PRINT
if is_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
#SECOND & THIRD LINE PRINT
check_left(chocolates, cups_of_milk)