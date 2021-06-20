import os.path
from os import path

#SOLUTION 1
if path.exists('file.txt'):
    print('File found')
else:
    print('File not found')



current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "..", "files", "exmaple.txt")

with open(path) as file:
    pass