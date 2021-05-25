# from collections import deque
#
# test_queue = deque(['a', 'b', 'c', 'd', 'e'])
# print(test_queue)
# test_queue.rotate(-2)
# print(test_queue)

from datetime import datetime, timedelta

time = datetime.strptime('00:00:00','%H:%M:%S')
print(time.time())

for i in range(5):
    time += timedelta(seconds=1)
    print(time.time())
