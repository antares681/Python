# CPU FOR PARALLEL COMPUTING

cpu_cores_nmbr = int(input())
files_list = [int(files) for files in input().split()]
file_limit_cpu = int(input())

used_cores_time = 0

files_list.sort(reverse=True)

for file_time in files_list[:file_limit_cpu]:
    if file_time >= cpu_cores_nmbr:
        used_cores_time += file_time / cpu_cores_nmbr
        files_list.pop(0)

for file_time in files_list:
    used_cores_time += file_time

print(f'{used_cores_time:.0f}')

#TEST CASES

#Case 1 - Original
# 4
# 4 1 3 2 8
# 1
#
#Case 2
# 4
# 8 8 8 8 8
# 4
#Case 3
# 4
# 8 8 8 8 8
# 1
#Case 4
# 4
# 1 1 1 1 1
# 5