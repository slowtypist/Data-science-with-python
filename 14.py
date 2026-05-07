#Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
final1 = string.find("P")
final2 = string.find("F")
final3 = string.find("E")


first = string[final1]

second = string[final2]

third = string[final3]
result = "".join([first , second , third])
print(result)

