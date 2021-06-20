data = list(map(int, input().split()))
print(data)
negatives = list(filter(lambda x: x < 0, data))
print(sum(negatives))
positives = list(filter(lambda x: x >=0, data))
print(sum(positives))

if sum(positives) > abs(sum(negatives)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")



