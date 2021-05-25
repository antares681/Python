operator_as_text = input()
num_1 = int(input())
num_2 = int(input())

result = 0

def calculator(opr, num1, num2):
    if opr == "multiply":
        result = num1 * num2
    elif opr == "divide":
        result = num1 / num2
    elif opr == "add":
        result = num1 + num2
    elif opr == "subtract":
        result = num1 - num2
    else:
        result = None

    return result

print(int(calculator(operator_as_text, num_1, num_2)))