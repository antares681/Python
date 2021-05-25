number_of_rooms = int(input())
charis_number = 0
counter_free_seats = 0
is_enough_seats = True

for room in range(number_of_rooms):
    chairs_number = input().split()
    counter_free_seats += len(chairs_number[0]) - int(chairs_number[1])
    if int(chairs_number[1]) > len(chairs_number[0]):
        is_enough_seats = False
        print(f'{int(chairs_number[1]) - len(chairs_number[0])} more chairs needed in room {room + 1}')
if is_enough_seats:
    print(f'Game On, {counter_free_seats} free chairs left')
