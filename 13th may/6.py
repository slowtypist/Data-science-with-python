lst = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]
print(lst)
print(len(lst))
first = lst[0]
mid = lst[len(lst)//2]
last = lst[len(lst)-1]
print(first,mid,last)
lst[4] = "jp morgan"
print(lst)
lst.append("lijjat")
lst.insert(len(lst)//2, "mercedes")
print(lst)
lst[0] = "FACEBOOK"
print(lst)
if "postamn api" in lst:
    print(True)
else:
    print(False)
lst.reverse()
print(lst)
print(lst[::-1])
lst2= lst[::-1]
print(lst2[::-1])
print(lst[0:4])
print(lst[6:9])
del lst[0:3]
print(lst)
del lst[-3:]
print(lst)
del lst[len(lst)-1]
print(lst)
lst.clear()
print(lst)
