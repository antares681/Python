# nmbr = int(input())
# periodic_table = set()
# for _ in range(nmbr):
#     data = input().split()
#     for element in data:
#         periodic_table.add(element)
# for el in periodic_table:
#     print(el)


nmbr = int(input())
periodic_table = set()
for _ in range(nmbr):
    data = input().split()
    for element in data:
        periodic_table.add(element)
[print(el) for el in periodic_table]
