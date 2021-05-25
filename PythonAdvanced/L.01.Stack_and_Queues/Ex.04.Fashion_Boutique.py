def push(rack_size,box):
    last_item = 0
    rack = []
    rack.append(int(box.pop()))
    rack_collection = []
    while box:
        rack.append(int(box.pop()))
        if rack_size < sum(rack):
            box.append(int(rack.pop()))
            rack_collection.append(sum(rack))
            rack = []
    if rack:
        rack_collection.append(sum(rack))
    return rack_collection

result = []

clothes_box = input().split(" ")
rack_size = int(input())
result = (push(rack_size, clothes_box))
print(len(result))