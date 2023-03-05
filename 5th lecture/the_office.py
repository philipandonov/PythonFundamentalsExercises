employee_happiness = input().split()
employee = int(input())
employee_happiness_to_int = list(map(int, employee_happiness))
happy_employee = list(
    filter(lambda x: x >= sum(employee_happiness_to_int) / len(employee_happiness_to_int), employee_happiness_to_int))
if len(happy_employee) >= len(employee_happiness_to_int)/2:
    print(f"Score: {len(happy_employee)}/{len(employee_happiness_to_int)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employee)}/{len(employee_happiness_to_int)}. Employees are not happy!")