#TODO EXAMPLE 1 - MAP
data = input()   #-> 1 2 3 4 5 6 7 8 9 10
print(list(map(lambda x: x+1, [int(x) for x in data.split()]))) #ADD 1 to WHOLE LIST

data = input()  #-> 1 2 3 4 5 6 7 8 9 10
print(list(map(lambda x: int(x), data.split())))    #CONVERT TO INT


#TODO EXAMPLE 2 - FILTER
data = input()  #-> 1 2 3 4 5 6 7 8 9 10
print(list(filter(lambda x: x % 2 == 0, [int(x) for x in data.split()])))

#TODO EXAMPLE 3 - SORTED
data = input()  #-> 1 2 3 4 5 6 7 8 9 10
print(sorted([int(x) for x in data.split()], reverse=True))


#TODO EXAMPLE 4  MAP





#TODO QUESTION
# Какъв е смисъла да се ползва:
# list(map(lambda x: int(x), data.split())) , щом си работи чудесно без ламбда така:
# list(map(int, data.split()))

