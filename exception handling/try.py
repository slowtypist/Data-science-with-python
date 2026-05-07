a = int(input("enter a number:"))
try:
    print(10/0) #using only try will get an error we use it with either except or finally
except ZeroDivisionError: #this will handle the zero division error only if there is exception
    print("you cannot divide by zero")
print(" done division")