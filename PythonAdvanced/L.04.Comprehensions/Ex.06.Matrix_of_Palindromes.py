rows, cols = input().split()
mx = [[f'{chr(j+97)}{chr(i+j+97)}{chr(j+97)}' for i in range(int(cols))] for j in range(int(rows))]

for el in range(len(mx)):
    print(" ".join([elem for elem in mx[el]]))