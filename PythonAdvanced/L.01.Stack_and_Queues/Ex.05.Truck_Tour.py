# def station_config(num_of_stations):
#     petrol_stations = []
#     for i in range(1, num_of_stations+1):
#         petrol_amount, km_next_station = input().split(' ')
#         petrol_stations.append([int(petrol_amount), int(km_next_station)])
#     return petrol_stations
#
# def reach_calculator(circle):
#     station_counter = 0
#     current_station = 0
#     valid = True
#     ttl_petrol_in_car = 0
#
#     for i in range(len(circle)):
#         petrol, km_next_station = circle[0][0], circle[0][1]
#         for i in range(len(circle)):
#             if petrol < km_next_station:
#                 circle.append(circle.popleft())
#                 station_counter += 1
#                 valid = False
#                 break
#             else:
#                 ttl_petrol_in_car += petrol - km_next_station
#                 if ttl_petrol_in_car < 0:
#                     valid = False
#                     station_counter = current_station *1
#                     break
#                 else:
#                     circle.append(circle.popleft())
#                     valid = True
#                     current_station +=1
#         if valid:
#             break
#     print(station_counter)
#
# from collections import deque
#
# range_per_liter = 1
# stations = int(input())
# circle = deque(station_config(stations))
# reach_calculator(circle)

# from collections import deque
#
# range_per_liter = 1
# petrol_stations = deque()
# valid = True
# station_counter = -1
# current_station_counter = 0
# petrol_in_car = 0
# finished = False
# stations = int(input())
#
# for i in range(0, stations):
#     petrol_amount, km_next_station = input().split(' ')
#     petrol_stations.append([float(petrol_amount), float(km_next_station)])
#
# for i in range(len(petrol_stations)): #БРОИ нач. станция
#     if finished:
#         break
#     station_counter +=1
#     petrol_in_car = 0
#     for i in petrol_stations: #БРОИ текущата станциия и дали вс. са ОК с бензина
#         petrol, km_next_station = petrol_stations[0][0], petrol_stations[0][1]
#         petrol_in_car += petrol - km_next_station
#         if petrol_in_car < 0:
#             petrol_stations.append(petrol_stations.popleft())
#             current_station_counter += 1
#             valid = False
#             break
#         else:
#             current_station_counter +=1
#             valid = True
#             finished = True
#
#         if not valid:
#             station_counter = current_station_counter
#             finished = False
#
# if valid:
#     print(station_counter)

# def station_config(num_of_stations):
#     petrol_stations = deque()
#     for i in range(num_of_stations):
#         petrol_amount, km_next_station = input().split(' ')
#         petrol_stations.append([int(petrol_amount), int(km_next_station)])
#     return petrol_stations
#
#
# def range_calculator(circle):
#     is_valid = True
#     for petrol_station_number in range(len(circle)):
#         petrol_in_car = 0
#         for _ in range(len(circle)):
#             petrol, km_next_station = int(circle[0][0]), int(circle[0][1])
#             petrol_in_car += petrol - km_next_station
#             if petrol_in_car < 0:
#                 circle.append(circle.popleft())
#                 is_valid = False
#                 break
#         if is_valid:
#             print(petrol_station_number)
#
#
# from collections import deque
#
# print(range_calculator(deque(station_config(int(input())))))
# from collections import deque
# circle = deque()
# num_of_stations = int(input())
#
# for i in range(num_of_stations):
#     petrol_amount, km_next_station = input().split(' ')
#     circle.append([int(petrol_amount), int(km_next_station)])
#
# for petrol_station_number in range(num_of_stations):
#     is_valid = True
#     petrol_in_car = 0
#     for station in range(num_of_stations):
#         petrol, km_next_station = int(circle[station][0]), int(circle[station][1])
#         petrol_in_car += petrol - km_next_station
#
#         if petrol_in_car < 0:
#             circle.append(circle.popleft())
#             is_valid = False
#             break
#     if is_valid:
#         print(petrol_station_number)
#         break
'''
11
1 5
1 3
1 4
3 10
1 5
1 3
1 4
3 10
1 5
1 3
250 25
'''

from collections import deque

queue = deque()
n = int(input())
for _ in range(n):
    gas_pump  = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])


