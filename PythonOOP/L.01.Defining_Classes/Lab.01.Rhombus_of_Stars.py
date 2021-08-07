# # TODO FUNCITONAL WAY OF WRITING CODE
def draw_rhombus(n):
    for i in range(n):
        offset = (n - i - 1) * ' '
        print(f'{offset}{("* " * (i + 1)).strip()}')

    for i in range(n - 2, -1, -1):
        offset = (n - i - 1) * ' '
        print(f'{offset}{("* " * (i + 1)).strip()}')
#
# draw_rhombus(int(input()))

# TODO OOP WAY OF WRITING CODE
# SPLITED THIS WAY CODE IS MORE READABLE, MISTAKES WILL NOT MULTIPLY

def generate_line(count, symbol, offset_count = 0):
    offset = offset_count * ' '
    return (f'{offset}{(symbol * count).strip()}')

def draw_line(count, symbol, offset_count = 0):
    print(generate_line(count, symbol, offset_count = 0))

def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, '* ', n - i -1)

    for i in range(n - 2, -1, -1):
        draw_line(i + 1, '* ', n - i - 1)

def draw_triangle(n):
    for i in range(n):
        draw_line(i + 1, '+ ')
    for i in range(n-1, -1, -1):
        draw_line(i + 1, '+ ')


n = int(input())
draw_rhombus(n)
draw_line(20, '+ ', 1)  # draw line method is REUSABLE!,
draw_triangle(n)