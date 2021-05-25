car_park = {}
number_of_cars = int(input())
max_milage = 100000
max_tank = 75
for i in range(number_of_cars):
    car_model, car_milage, car_fuel = input().split('|')
    car_milage, car_fuel = int(car_milage), int(car_fuel)
    car_park[car_model] = [car_milage, car_fuel]

command = input()
while not command == 'Stop':
    command = command.split(' : ')
    instruction = command[0]

    if instruction == 'Drive':
        car, distance, fuel = command[1], command[2], command[3]
        distance, fuel = int(distance), int(fuel)
        if not fuel < car_park[car][1]:
            print(f"Not enough fuel to make that ride")
        else:
            car_park[car][1] -= fuel
            car_park[car][0] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if car_park[car][0] >= max_milage:
                print(f'Time to sell the {car}!')
                del car_park[car]

    elif instruction == 'Refuel':
        car, fuel = command[1], command[2]
        fuel = int(fuel)
        if car_park[car][1] + fuel < max_tank:
            diff_fuel = fuel
            car_park[car][1] += fuel
        else:
            diff_fuel = 75 - car_park[car][1]
            car_park[car][1] = 75
        print(f"{car} refueled with {diff_fuel} liters")

    elif instruction == 'Revert':
        car, kilometers = command[1], command[2]
        kilometers = int(kilometers)
        diff = 10000 - car_park[car][0]
        car_park[car][0] -= kilometers
        if not car_park[car][0] < 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            car_park[car][0] = 10000
    command = input()

sorted_car_park = sorted(car_park.items(), key=lambda x: (-x[1][0], x[0]))

for c,d in sorted_car_park:
    print(f"{c} -> Mileage: {d[0]} kms, Fuel in the tank: {d[1]} lt.")