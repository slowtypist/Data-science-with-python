ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
sum = 0
average_sum = 0
for i in ages:
    sum=sum+i

average_sum= sum/len(ages)
print(average_sum)
