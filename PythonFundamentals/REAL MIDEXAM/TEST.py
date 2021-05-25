# print(2**31)
# print(-2**31)

ll = [1,2,6,7,98,4,32,1,3,45,65,123,4,5,12]

for _ in range(len(ll)):
    for i in range(len(ll)-1):
        if ll[i] < ll[i+1]:
            ll[i], ll[i+1] = ll[i+1], ll[i]


print(ll)