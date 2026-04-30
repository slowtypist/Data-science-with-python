d = {1:11, 2:22, 3:33}
d.update({1:89})
d[90] = 765 #here we are creating a key and its value in dict 
del d[2] #here we are deleting the key and its value from dict
print(d)