l = [12,16,13,19]
largest = l[0]
second_largest= l[1]
for i in l:
    if i> largest:
        second_largest = largest
        largest = i
    elif i>second_largest : #because if i add anything at last that is lesser than 19 it wont come in seconf largest
        second_largest = i

print(second_largest , largest)
