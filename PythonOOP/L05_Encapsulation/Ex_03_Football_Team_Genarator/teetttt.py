a = ['a', 'b', 'c', 'd']

for i in range(len(a)-1):
    if a[i] == 'c':
        print(a.pop(i))
    print(a)
