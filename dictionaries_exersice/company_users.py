company_names = {}
command = input()
while command != "End":
    company, id = command.split(" -> ")
    if company not in company_names.keys():
        company_names[company] = []

    if id not in company_names[company]:
        company_names[company].append(id)

    command = input()
for key in company_names:
    print(f"{key}")
    for value in company_names[key]:
        print(f"-- {value}")


