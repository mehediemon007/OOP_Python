from Employee import *

employee1 = EmployeeDetails("Abdul Satter", "0182134455", 29, "Dhonkunti,Sherpur,Bogura", "21/1/2018", 10000, 500)

print(employee1.name, employee1.mobileNumber, employee1.age, employee1.address, employee1.joinDate)
print(employee1.total_monthly_salary())
