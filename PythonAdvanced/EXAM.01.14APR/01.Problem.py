def pizza_checker(orders_left):
    if sum(orders_left) <= 0:
        return False
    return True

def empl_checker(free_empl):
    if len(free_empl) <= 0:
        return False
    return True

def solve(pizza_orders, employees_capacity):
    total_pizzas_made = 0
    while len(employees_capacity) and len(pizza_orders):

        if pizza_orders[0] <= employees_capacity[-1]:
            total_pizzas_made += pizza_orders.pop(0)
            employees_capacity.pop()
        else:
            total_pizzas_made += employees_capacity[-1]
            pizza_orders[0] = abs(pizza_orders[0] - employees_capacity.pop())

    if not empl_checker(employees_capacity):
        print(f"Not all orders are completed.")
        print(f"Orders left: {', '.join(map(str, pizza_orders))}")

    if not pizza_checker(pizza_orders):
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {total_pizzas_made}")
        print(f"Employees: {', '.join(map(str, employees_capacity))}")

pizza_orders = [x for x in map(int, input().split(', ')) if x < 11 and x > 0]
employees_capacity = [x for x in map(int, (input().split(', '))) if x >= 0]
solve(pizza_orders, employees_capacity)

#TODO TEST INPUTS

# 10, 9, 8, 7, 5
# 5, 10, 9, 8, 7


# 12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1


