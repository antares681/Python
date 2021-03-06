def jackpot(left, right, match):
    for char in match:
        if char * 10 in left and char * 10 == right:
            print( f'ticket "{ticket}" - 10{char} Jackpot!' )
            return True
    return False


def win(left, right, match):
    for char in match:
        if char * 6 in left and char * 6 in right:
            print( f'ticket "{ticket}" - {min(adjacent_symbols(right), adjacent_symbols(left))}{char}')
            return True
    return False

def adjacent_symbols(side):
    iterator = 1
    final_list = []
    for index in range(len(side) - 1):
        if side[index] == side[index+1]:
            iterator += 1
        else:
            final_list.append(iterator)
            iterator = 1
    final_list.append(iterator)
    return max(final_list)

matching_list = ['@','#','$','^']
tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) == 20:
        left_side = ticket[0:10]
        right_side = ticket[10:]
        if jackpot(left_side, right_side, matching_list):
            continue
        elif win(left_side , right_side , matching_list):
            continue
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")

