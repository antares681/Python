# size_of_side = float(input())
# n_sheets_of_paper = int(input())
# counter = 0
# total_sheet_area = 0
# # To find the surface area of a cuboid, add the areas of all 6 faces.
# # We can also label the length (l), width (w), and height (h) of the prism and use the formula,
# # SA=2lw+2lh+2hw, to find the surface area.
# box_area = size_of_side * size_of_side * 6  # As stated in the comment
#
# for sheet in range(n_sheets_of_paper):
#
#     length_sheet = float(input())
#     width_sheet = float(input())
#     sheet_area = length_sheet * width_sheet  # Area=L*W
#     counter += 1
#
#     if counter % 3 == 0:  # every 3rd
#         sheet_area = sheet_area * 0.75  # cover only 25%
#
#     if counter % 5 == 0:  # every 5th
#         sheet_area = 0  # cannot be used
#
#     total_sheet_area += sheet_area
#
# box_covered = total_sheet_area - box_area
# percentage = (1 - (total_sheet_area / box_area)) * 100
# # print(percentage)
# if box_covered >= 0:
#     print("You've covered the gift box!")
#     print(f"{percentage:.2f}% wrap paper left.")
# else:
#     print("You are out of paper!")
#     print(f"{percentage:.2f}% of the box is not covered.")

# cube_side = float(input())
# cube_surface = 6*(cube_side*cube_side)
# num_papers = int(input())
# counter_papers = 1
# percentage_covered =[]
# paper_max = 1
# ttl_paper_area = 0
# for paper in range(num_papers):
#     paper_length = float(input())
#     paper_width = float(input())
#     paper_area = paper_width * paper_length
#     if counter_papers % 3 == 0:
#         percentage = float((paper_length*paper_width * 0.75) / cube_surface)
#         percentage_covered.append(percentage)
#     if counter_papers % 5 == 0:
#         continue
#     else:
#         percentage = float(paper_area / cube_surface)
#         percentage_covered.append(percentage)
#     ttl_paper_area += paper_area
#
#     counter_papers += 1
#
#     if paper_max <= sum(percentage_covered):
#         break
#
# if ttl_paper_area - cube_surface <= 0:
#     result = (ttl_paper_area / cube_surface) * 100
#     print(f"You are out of paper!\n{abs(result):.2f}% of the box is not covered.")
#
#
# else:
#     result = (ttl_paper_area - cube_surface) / ttl_paper_area * 100
#     print(f"You've covered the gift box!\n{abs(result):.2f}% wrap paper left.")

# cube_side = float(input())
# cube_surface = 6*(cube_side**2)
# num_papers = int(input())
# counter_papers = 1
# percentage_covered =[]
# paper_max = 1
# ttl_paper_area = 0
#
# for paper in range(num_papers):
#     paper_length = float(input())
#     paper_width = float(input())
#     paper_area = paper_width * paper_length
#     ttl_paper_area += paper_area
#     if counter_papers % 5 == 0:
#         continue
#     elif counter_papers % 3 == 0:
#         percentage = (paper_length * paper_width) * 0.75
#         percentage_covered.append(percentage)
#     else:
#         percentage = paper_area / cube_surface
#         percentage_covered.append(percentage)
#     if paper_max <= sum(percentage_covered):
#         break
#     counter_papers += 1
#
# difference = (paper_max - sum(percentage_covered))*100
# if not difference <= 0:
#     print(f"You've covered the gift box!\n{abs(difference):.2f}% wrap paper left.")
#
# else:
#     result = (ttl_paper_area - cube_surface) / ttl_paper_area * 100
#     print(f"You've covered the gift box!\n{abs(result):.2f}% wrap paper left.")

# cube_side = float(input())
# cube_surface = 6*(cube_side * cube_side)
#
# num_papers = int(input())
# counter_papers = 1
# percentage_covered =[]
# necessary_paper = 1.00 #in percent 100%
# ttl_paper_area = 0
#
# for paper in range(num_papers):
#     paper_length = float(input())
#     paper_width = float(input())
#     paper_area = paper_width * paper_length
#     ttl_paper_area += paper_area
#
#     if counter_papers % 5 == 0:
#         continue
#     elif counter_papers % 3 == 0:
#         percentage = (paper_area * 0.75) / cube_surface
#         percentage_covered.append(percentage)
#     else:
#         percentage = paper_area / cube_surface
#         percentage_covered.append(percentage)
#
#     if necessary_paper <= sum(percentage_covered):
#         break
#     counter_papers += 1
#
# difference = (necessary_paper - sum(percentage_covered))*100
# if difference > 0:
#     print(f"You are out of paper!\n{abs(difference):.2f}% of the box is not covered.")
#
# else:
#     result = (ttl_paper_area - cube_surface) / ttl_paper_area * 100
#     print(f"You've covered the gift box!\n{abs(result):.2f}% wrap paper left.")
#
# '''
# 10
# 5
# 3
# 0.5
# 2.4
# 5
# 3.7
# 1
# 3
# 34.7
# 5
# 80
#
# '''
from collections import deque
stations = deque([])
n = int(input())

for _ in range(n):
    stations.append([el for el in input().split()])

for big_circle_iteration in range(n):
    is_valid = True
    tank_petrol = 0
    for small_circle_iteration in range(n):
        tank_petrol += int(stations[small_circle_iteration][0]) - int(stations[small_circle_iteration][1])

        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    if is_valid:
        print(big_circle_iteration)
        break