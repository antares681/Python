activity = input()
activity_list_lower = ['coding', 'dog', 'cat', 'movie']
activity_list_upper = ['CODING', 'DOG', 'CAT', 'MOVIE']
event_counter = 0
item = 0

while not activity == "END":
    for i in activity_list_upper:
        if activity == activity_list_upper[item]:
            event_counter += 2
        item+=1
    item = 0
    for i in activity_list_lower:
        if activity == activity_list_lower[item]:
            event_counter += 1
        item += 1
    item = 0

    if event_counter < 5:
       activity = input()
    else:
        print('You need extra sleep')
        break
else:
    print(event_counter)
#
# activity = input()
# activity_list_lower = ['coding', 'dog', 'cat', 'movie']
# activity_list_upper = ['CODING', 'DOG', 'CAT', 'MOVIE']
# event_counter = 0
#
# while not activity == "END":
#     if activity in activity_list_upper:
#             event_counter += 2
#     elif activity in activity_list_lower:
#             event_counter += 1
#
#     if event_counter <= 5:
#        activity = input()
#     else:
#         print('You need extra sleep')
#         break
# else:
#     print(event_counter)