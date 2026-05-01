a = int(input("enter a number:"))
try:
    print(10/a) #using only try will get an error we use it with either except or finally
except Exception as error : #this will handle all the exceptions
    print("sorry there is an error",error)
else: #else will execute only if there is no exception
    print("division is successful")
finally: #finally will execute whether there is an exception or not
    print("this will execute no matter what")
print(" done division")