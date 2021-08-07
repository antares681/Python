from math import floor
def flights(*args):
    my_dict = {}
    data = [el for el in args]
    for _ in range(floor(len(data)/2)):
        key, val = data.pop(0), data.pop(0)
        if not key == 'Finish':
            if key in my_dict:
                my_dict[key] += val
            else:
                my_dict[key] = val
        else:
            break
    return my_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
