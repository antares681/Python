ttl_capacity = 255
rest_capacity = 255
n = int(input())

for i in range (0, n):
    water_quantity = int(input())
    if water_quantity > rest_capacity:
        print('Insufficient capacity!')
    elif water_quantity <= water_quantity:
        rest_capacity -= water_quantity

print(ttl_capacity - rest_capacity)