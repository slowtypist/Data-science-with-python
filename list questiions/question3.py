l = [1,2,3,4,5,6,7,8]
greatst = l[0]
index = 0
for i in range(len(l)):
    if l[i]>greatst:
        greatst = l[i]
        index = i
print(greatst)


