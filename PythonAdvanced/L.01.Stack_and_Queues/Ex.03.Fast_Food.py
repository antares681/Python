def solve(food, orders):
    biggest_order = 0
    while orders:
        curr_order = orders.popleft()
        if food >= curr_order:
            food -= curr_order
        else:
            orders.appendleft(curr_order)
            if not biggest_order > max(orders):
                biggest_order = max(orders)
            return biggest_order, orders
        if curr_order > biggest_order:
            biggest_order = curr_order

    return biggest_order, 'complete'

#GET INPUT DATA
from collections import deque
orders = deque()

quantity_of_food = int(input())
orders_list = deque([int(i) for i in input().split(' ')])

#RUN PROGRAM
biggest_order, orders_left = solve(quantity_of_food, orders_list)

#PRINT RESULT
print(f'{biggest_order}')
if not orders_left == 'complete':
    orders_left = ' '.join([str(i) for i in orders_left])
    print(f'Orders left: {orders_left}')
else:
    print('Orders complete')



''' 
TEST INPUT

 348
20 54 30 16 7 9
'''

#TODO От условието не е ясно дали ако някоя поръчка не може да бъде изпълнена се прекратява обслужването и се печата резултат или се продължава към следващата поръчка докато се обходи опашката и се изпълнята всички възможни поръчки.
