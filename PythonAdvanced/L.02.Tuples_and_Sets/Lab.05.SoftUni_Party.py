#TODO SOLUTION 1
def guest_Sorter(guests_nmbr):
    vip_guestlist = set()
    standard_guestlist = set()
    for _ in range(guests_nmbr):

        reservation = input()
        if reservation[0].isdigit():
            vip_guestlist.add(reservation)
        elif reservation[0].isalpha():
            standard_guestlist.add(reservation)

    return standard_guestlist, vip_guestlist

def entry_Control(vips, standards):
    data = input()
    while not data == 'END':
        if data in vips:
            vips.remove(data)
        elif data in standards:
            standards.remove(data)
        data = input()
    return vips | standards

sep = "\n"
list_standard, list_vip = guest_Sorter(int(input()))
absent_guests = entry_Control(list_vip, list_standard)
print(f'{len(absent_guests)}\n{sep.join(sorted(absent_guests))}')


#TODO SOLUTION 2

# def guest_Sorter(guests_nmbr):
#     guestlist = set()
#     for _ in range(guests_nmbr):
#         reservation = input()
#         guestlist.add(reservation)
#     return guestlist
#
# def entry_Control(guests):
#     data = input()
#     while not data == 'END':
#         if data in guests:
#             guests.remove(data)
#         data = input()
#     return list(guests)
#
# sep = "\n"
# guest_list = guest_Sorter(int(input()))
# absent_guests = entry_Control(guest_list)
# print(f'{len(absent_guests)}\n{sep.join(sorted(absent_guests))}')
