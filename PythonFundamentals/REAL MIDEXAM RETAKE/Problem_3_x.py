#SOLUTION 2

neighbrhd = [int(house) for house in input().split('@')]
cur_loc_idx = 0
neighbrhd_size = len(neighbrhd)

while True:
    command = input().split(" ")
    if command[0] == "Love!":
        break
    if command[0] == "Jump":
        jump_length = int(command[1])

        cur_loc_idx += jump_length
        if 0 <= cur_loc_idx < neighbrhd_size:
            if neighbrhd[cur_loc_idx] > 0:
                neighbrhd[cur_loc_idx] -= 2
                if neighbrhd[cur_loc_idx] == 0:
                    print(f"Place {cur_loc_idx} has Valentine's day.")
            else:
                print(f"Place {cur_loc_idx} already had Valentine's day.")
        else:
            cur_loc_idx = 0
            if neighbrhd[cur_loc_idx] > 0:
                neighbrhd[cur_loc_idx] -= 2
                if neighbrhd[cur_loc_idx] == 0:
                    print(f"Place {cur_loc_idx} has Valentine's day.")
            else:
                print(f"Place {cur_loc_idx} already had Valentine's day.")

print(f"Cupid's last position was {cur_loc_idx}.")

if not sum(neighbrhd) == 0:
    print(f'Cupid has failed {neighbrhd_size - neighbrhd.count(0)} places.')

else:
    print(f'Mission was successful.')