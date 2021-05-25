def adder(p,c,k,r):
    if not p in r:
        r[p] = [c, k]
        print(f"{p} by {c} in {k} added to the collection!")
    else:
        print(f'{p} is already in the collection!')
    return r

def remover(p, r):
    if p in r:
        print(f"Successfully removed {p}!")
        r.pop(p)
    else:
        print(f"Invalid operation! {p} does not exist in the collection.")
    return r

def keychanger(p,k,r):
    if not p in r:
        print(f"Invalid operation! {p} does not exist in the collection.")
    else:
        r[p][1] = k
        print(f"Changed the key of {p} to {k}!")
    return r

n = int(input())
repertoire = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    repertoire[piece] =[composer, key]

command = input()

while not command == 'Stop':
    command = command.split('|')
    event = command[0]
    piece = command[1]
    if event == 'Add':
        composer = command[2]
        key = command[3]
        repertoire = adder(piece, composer, key, repertoire)
    elif event == 'Remove':
        repertoire = remover(piece, repertoire)
    elif event == 'ChangeKey':
        new_key = command[2]
        repertoire = keychanger(piece, new_key, repertoire)
    command = input()

sorted_repertoire = sorted(repertoire.items(), key = lambda pc: (pc[0], pc[1][0]))

for p, a in sorted_repertoire:
    print(f"{p} -> Composer: {a[0]}, Key: {a[1]}")