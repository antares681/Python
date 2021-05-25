def rows_checker(first_row, second_row, third_row):
    #row checks
    if first_row[0] == first_row[1] == first_row[2] != 0:
        return first_row[0]
    elif second_row[0] == second_row[1] == second_row[2] != 0:
        return second_row[0]
    elif third_row[0] == third_row[1] == third_row[2] != 0:
        return third_row[0]

    #column checks
    if first_row[0] == second_row[0] == third_row[0] != 0:
        return first_row[0]
    elif first_row[1] == second_row[1] == third_row[1] != 0:
        return first_row[1]
    elif first_row[2] == second_row[2] == third_row[2] != 0:
        return first_row[2]

    #diagonal checks
    if first_row[0] == second_row[1] == third_row[2] != 0:
        return first_row[0]
    elif first_row[2] == second_row[1] == third_row[0] != 0:
        return first_row[2]

    else:
        return('Draw!')

def result_analyzer(value):
    if value == 1:
        return 'First player won'
    if value == 2:
        return 'Second player won'
    if value == 'Draw!':
        return 'Draw!'

row_1 = [int(i) for i in input().split(" ")]
row_2 = [int(i) for i in input().split(" ")]
row_3 = [int(i) for i in input().split(" ")]

print(result_analyzer(rows_checker(row_1, row_2, row_3)))

