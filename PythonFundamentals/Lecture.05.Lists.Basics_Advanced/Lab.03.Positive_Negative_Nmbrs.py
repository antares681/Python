lines_number = int(input())
list_negatives= []
list_positives=[]
sum_negatives = 0
count_positives = 0
for i in range (lines_number):
    num = int(input())
    if num < 0:
        list_negatives.append(num)
    else:
        list_positives.append(num)
print(list_positives)
print(list_negatives)
print(f'Count of positives: {len(list_positives)}. Sum of negatives: {sum(list_negatives)}')