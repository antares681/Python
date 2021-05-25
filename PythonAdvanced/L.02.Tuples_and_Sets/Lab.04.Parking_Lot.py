# car_number = int(input())
# parking_lot = set()
# for _ in range(car_number):
#     mvt, plate = input().split(', ')
#     if mvt == 'IN':
#         parking_lot.add(plate)
#     elif mvt == 'OUT':
#         parking_lot.remove(plate)
# if parking_lot:
#     print('\n'.join(parking_lot))
# else:
#     print('Parking Lot is Empty')

#TODO SOLUTION 2

car_number = int(input())
parking_lot = set()
mvt_type = {'IN':parking_lot.add, 'OUT':parking_lot.remove}
for _ in range(car_number):
    mvt, plate = input().split(', ')
    mvt_type[mvt](plate)
if parking_lot:
    print('\n'.join(parking_lot))
else:
    print('Parking Lot is Empty')