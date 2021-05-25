from datetime import datetime, timedelta
from collections import deque

data = input().split(';')
robots = {k:int(v) for k, v in [el.split('-') for el in data]}
available_robots = {k: 0 for k in robots}
tasks = deque()
time = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=1)

product = input()
while not product == 'End':
    tasks.append(product)
    product = input()

while tasks:
    availability_list = [robot for robot,time in available_robots.items() if time <=0]
    if availability_list:
        print(f"{availability_list[0]} - {tasks.popleft()} [{time.strftime('%H:%M:%S')}]")
        available_robots[availability_list[0]] = robots[availability_list[0]]
        time += timedelta(seconds=1)
        available_robots = {k:v -1 for k, v in available_robots.items()}
    else:
        while not availability_list:
            available_robots = {k: v - 1 for k, v in available_robots.items()}
            time +=timedelta(seconds=1)
            availability_list = [k for k, v in available_robots.items() if v <=0]






