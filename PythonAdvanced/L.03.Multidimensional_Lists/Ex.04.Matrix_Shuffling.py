rows, cols = map(int, input().split(' '))
mx = [[el for el in input().split(' ')] for _ in range(rows)]

command = input()

while not command == 'END':
    if len(command.split()) == 5:
        action, coor_x0, coor_y0, coor_x1, coor_y1 = [int(el) if el.isdigit() else el for el in command.split(' ')]

        if action == 'swap' and not coor_x0 > rows and not coor_y0 > cols and not coor_x1 > rows and not coor_y1 > cols:
            temp_coor = mx[coor_x0][coor_y0]
            mx[coor_x0][coor_y0] = mx[coor_x1][coor_y1]
            mx[coor_x1][coor_y1] = temp_coor
            for i in range(len(mx)):
                print(' '.join(mx[i]))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    command = input()