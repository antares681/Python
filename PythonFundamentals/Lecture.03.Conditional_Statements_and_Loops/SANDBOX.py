text = input()
y = ['vegas','London','US','UK']
i=0
for x in y:
    if text == y[i]:
        print(y[i])
        break
    else:
        i+=1