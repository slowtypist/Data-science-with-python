a = int(input("enter a number:"))
try:
    print(10/0) #using only try will get an error we use it with either except or finally
except Exception as error : #this will handle all the exceptions
    print("sorry there is an error",error)
print(" done division")