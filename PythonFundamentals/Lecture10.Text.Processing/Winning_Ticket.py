winning_symbols = ["@", "#", "$", "^"]

def jackpot_check(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
                return True
    return False

def winning_tkt_check(ticket):
    left_part = ticket[:10]
    right_part = ticket[10:]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_part and winning_symbol * 6 in right_part:
            left_symbols_count = left_part.count(winning_symbol)
            right_symbols_count = right_part.count(winning_symbol)
            match_result = min(left_symbols_count, right_symbols_count)
            print(f"ticket \"{ticket}\" - {match_result}{winning_symbol}")
            return True
    return False

tickets_list = [tkt.strip() for tkt in input().split(", ")]

for ticket in tickets_list:
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if jackpot_check(ticket):
        continue

    if winning_tkt_check(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")

# tickets_list = input().split(', ')
# symbols = ['@', '#', '$', '^']


# def symbol_check(ticket):
#     for symbol in symbols:
#         if symbol in ticket:
#             return symbol
#     return f'ticket "{ticket}" - no match'

# def consequitve_symbol(side):
#     check_result = []
#     counter = 1
#     for index in range(len(side) - 1):
#         if side[index] == side[index+1] and side[index] in symbols:
#             counter += 1
#         else:
#             check_result.append(counter)
#             counter = 1
#     check_result.append(counter)
#     return max(check_result)
#
# def ticket_validator(ticket, symbol):
#     left = ticket[:len(ticket) // 2 + 1]
#     right = ticket[len(ticket) // 2:]
#     count_left = consequitve_symbol(left)
#     count_right = consequitve_symbol(right)
#     if count_left >=6 and count_right >= 6:
#             return f'ticket "{ticket}" - {min(count_left, count_right)}{symbol}'
#         else:
#             return f'ticket "{ticket}" - no match'
#
#
# for ticket in tickets_list:
#     ticket = ticket.strip()
#     if not len(ticket) == 20:
#         print('invalid ticket')
#         continue
#     else:
#         for symbol in symbols:
#             if not symbol in ticket:
#                 continue
#             else:
#                 if symbol*20 == ticket:
#                     print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
#                 else:
#                     print(ticket_validator(ticket, symbol))
#
