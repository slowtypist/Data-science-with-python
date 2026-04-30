a = [12,13,14,15]
for i in range (len(a)-1): # so that it doesnt go out of range after 15 as its the last index
    if a[i] < a[i+1]:
            continue 
    else:
          print("your list is not sorted")
          break
else:
    print("your list is sorted")
    
    