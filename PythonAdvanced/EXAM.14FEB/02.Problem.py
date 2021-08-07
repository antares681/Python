#form matrix_cols
x_row_coor, y_col_coor = 0, 0
curr_coor_x, curr_coor_y = 0, 0
n = int(input())

mx = [(input().split()) for rows in range(n)]
counter = 0
while True:
    if counter < 100:
        command = input()
            if command == 'left':
                x_row_coor -= 1
            elif command == 'right':
                x_row_coor += 1
            elif command  == 'up':
                y_col_coor -= 1
            elif command == 'down':
                y_col_coor += 1
    else:
        break

    curr_coor_x = curr_coor_x + x_row_coor
    curr_coor_y = curr_coor_y + y_col_coor