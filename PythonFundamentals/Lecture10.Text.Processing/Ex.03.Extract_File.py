url_data = input().split("\\")
file_data = url_data[-1].split('.')
print(f'File name: {file_data[0]}\nFile extension: {file_data[1]}')