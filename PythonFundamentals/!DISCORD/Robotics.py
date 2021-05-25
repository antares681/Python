from collections import deque

food = int(input())

queue = deque([int(el) for el in input().split()])
biggest_order = max(queue)
print(biggest_order)
while queue:
    current_order = queue.popleft()

    if food >= current_order:
        food -= current_order
    else:
        queue.appendleft(current_order)
        print(f"Orders left: {' '.join(list(map(str, queue)))}")
        break

if not queue:
    print(f"Orders complete")



# SOLUTION

from collections import deque
from datetime import datetime, timedelta
data = input().split(";")
robots = {sub.split("-")[0]: int(sub.split("-")[1]) for sub in data}
available_robots = {k: 0 for k in robots}
tasks = deque()
timed = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=1)
command = input()
while command != "End":
    tasks.append(command)
    command = input()

while tasks:
    available = [k for k, v in available_robots.items() if v <= 0]
    if available:
        print(f"{available[0]} - {tasks.popleft()} [{timed.strftime( '%H:%M:%S' )}]")
        available_robots[available[0]] = robots[available[0]]
        timed += timedelta(seconds=1)
        available_robots = {k: v - 1 for k, v in available_robots.items()}
    else:
        while not available:
            tasks.append(tasks.popleft())
            available_robots = {k: v - 1 for k, v in available_robots.items()}
            timed += timedelta(seconds=1)
            available = [k for k, v in available_robots.items() if v <= 0]