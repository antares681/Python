import os
my_dict = {}
dirs = os.listdir('D:\PROJECTS\Python\PythonAdvanced\L.06.File_Handling\Exercises\Example')
for el in dirs:
     temp_tup = os.path.splitext(el)
     if not temp_tup[1] in my_dict:
        my_dict[temp_tup[1]] = []
     my_dict[temp_tup[1]].append((temp_tup[0]))

sorted_dict = sorted(my_dict.items(), key=lambda x: (x[0], x[1]))
for k, v in sorted_dict:
    with open('report.txt', 'a') as file:
        file.writelines(f'{k}\n')
        for el in v:
            file.writelines(f'- - - {el}{k}\n')