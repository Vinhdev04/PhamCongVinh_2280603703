hours_worked = float(input("Enter the number of hours worked: "))
salary = float(input("Enter the hourly salary: "))
hours_week = 44
hours_add = max(0, hours_worked - hours_week)

sumSalary = (hours_week * salary + hours_add * salary * 1.5)
print("The weekly salary is: ", sumSalary)