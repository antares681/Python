soldiers_list = input().split(" ")
position_step = int(input())
result = []
position = 0

while len(soldiers_list) > 0:
    position -= 1
    position = (position + position_step) % len(soldiers_list)
    result.append(soldiers_list.pop(position))
print(f"[{','.join(result)}]")