#Insert an IT company in the middle of the companies list
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]


mid_index = len(companies)//2
print(mid_index)
mid_element = companies[len(companies)//2]
print(mid_element)
companies.insert(mid_index,"jp")
print(companies.index("jp"))
print(companies)