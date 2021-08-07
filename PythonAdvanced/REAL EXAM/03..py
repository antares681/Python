mx = [input().split() for c in range(5)]
nums = int(input())
coordinates = []
target = 0


def locate_x_coor(m):
    cl = 0
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 'x':
                cl += 1
    return cl

cl = locate_x_coor(mx)

def find_person(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 'A':
                return row, col


def solve(cmd, rw, cl, m):
    global target
    global coordinates
    if len(cmd) == 3:
        X, position, num = cmd
        num = int(num)
        if position == 'right' and cl + num < len(m) and m[rw][cl + num] == '.':
            cl += num
        elif position == 'left' and cl - num >= 0 and m[rw][cl - num] == '.':
            cl -= num
        elif position == 'up' and rw - num >= 0 and m[rw - num][cl] == '.':
            rw -= num
        elif position == 'down' and rw + num < len(m) and m[rw + num][cl] == '.':
            rw += num

    else:
        X, position = command
        if position == 'left':
            for locate in range(cl, -1, -1):
                if m[rw][locate] == 'x':
                    m[rw][locate] = '.'
                    target += 1
                    coordinates.append(f"[{rw}, {locate}]")
                    break
        elif position == 'right':
            for locate in range(cl, len(m)):
                if m[rw][locate] == 'x':
                    m[rw][locate] = '.'
                    target += 1
                    coordinates.append(f"[{rw}, {locate}]")
                    break
        elif position == 'up':
            for locate in range(rw, -1, -1):
                if m[locate][cl] == 'x':
                    m[locate][cl] = '.'
                    target += 1
                    coordinates.append(f"[{locate}, {cl}]")
                    break
        elif position == 'down':
            for locate in range(rw, len(m)):
                if m[locate][cl] == 'x':
                    m[locate][cl] = '.'
                    target += 1
                    coordinates.append(f"[{locate}, {cl}]")
                    break
    return rw, cl, m
starting_row, start_col = find_person(mx)
for _ in range(nums):
    if locate_x_coor(mx) == 0:
        break
    command = input().split()
    starting_row, start_col, mx = solve(command, starting_row, start_col, mx)
if cl == len(coordinates):
    print(f'Training completed! All {cl} targets hit.')
else:
    print(f'Training not completed! {cl - len(coordinates)} targets left.')
[print(col) for col in coordinates]