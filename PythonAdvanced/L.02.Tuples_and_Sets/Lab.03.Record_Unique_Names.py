nmbr = int(input())
names = set()

for _ in range(nmbr):
    name = input()
    if name not in names:
        print(name)
        names.add(name)