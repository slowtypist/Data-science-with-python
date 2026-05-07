#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

string ="You cannot end a sentence with because because because is a conjunction"
first =  string.find("because")
second = string.find("because", first + 1)
third = string.find("because", second + 1)


print(string[first:third+len("because")])
