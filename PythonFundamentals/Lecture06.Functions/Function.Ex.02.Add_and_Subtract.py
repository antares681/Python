def sum_numbers (num1, num2):
    result_sum = num1 + num2
    return result_sum

def subtract_number(num1, num2):
    result_subtract = num1 - num2
    return result_subtract

def add_subtract(num1, num2, num3):
    result_sum = sum_numbers(num1, num2)
    result_subtraction = subtract_number(result_sum, num3)
    return result_subtraction

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result_calc = add_subtract(num_1, num_2, num_3)

print(result_calc)
