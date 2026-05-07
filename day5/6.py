#Print the number of companies in the list

companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]
print(len(companies))
print(companies.count("Facebook"))


first_company = companies[0]
middle_company = companies[len(companies)//2]
last_company = companies[len(companies)-1]

print(first_company,middle_company,last_company)

#Print the list after modifying one of the companies
companies[1] = "tcs"
print(companies)


#Add an IT company to it_companies
print(companies.append("jp morgan"))