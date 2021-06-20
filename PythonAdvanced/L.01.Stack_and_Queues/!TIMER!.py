from datetime import datetime, timedelta

time = datetime.strptime('00:00:00','%H:%M:%S')
# time = datetime.strptime(input(),'%H:%M:%S')  #TODO INPUT '00:00:00'
print(time.time())

for i in range(5):
    time += timedelta(seconds=1)
    print(time.time())
    print()