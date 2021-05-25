def valentine_check():
    if neigbrhd[curr_loct_idx] > 0:
        neigbrhd[curr_loct_idx] -= 2
        if neigbrhd[curr_loct_idx] == 0:
            return f"Place {curr_loct_idx} has Valentine's day."
        else:
            return f"Place {curr_loct_idx} already had Valentine's day."

neigbrhd = [int(house) for house in input().split('@')]
curr_loct_idx = 0
neigbrhd_size = len(neigbrhd)

while True:
    command = input().split(" ")
    if command[0] == "Love!":
        break
    if command[0] == "Jump":
        jump_length = int(command[1])
        curr_loct_idx += jump_length
        if 0 <= curr_loct_idx < neigbrhd_size:
            print(valentine_check())
        else:
            curr_loct_idx = 0
            print(valentine_check())
print(f"Cupid's last position was {curr_loct_idx}.")

if not sum(neigbrhd) == 0:
    print(f'Cupid has failed {neigbrhd_size - neigbrhd.count(0)} places.')
else:
    print(f'Mission was successful.')