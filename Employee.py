class EmployeeSalary:

    def __init__(self, name, baseSalary, bonus):
        self.name = name
        self.baseSalary = baseSalary
        self.bonus = bonus

    def monthly_salary(self):

        return self.baseSalary+(self.bonus*2)


class EmployeeDetails:

    companyName = "EasyTech"

    def __init__(self, name, mobileNumber, age, address, joinDate, baseSalary, bonus):
        self.name = name
        self.mobileNumber = mobileNumber
        self.age = age
        self.address = address
        self.joinDate = joinDate
        # composition..
        self.employeeSalary = EmployeeSalary(name, baseSalary, bonus)
        # innerclass..
        self.employeePhoneType = self.EmployeePhoneType("Xiaomi Note7", "3gb", "32gb")

    def total_monthly_salary(self):
        return self.employeeSalary.monthly_salary()

    class EmployeePhoneType:

        def __init__(self, phoneName, ram, rom):
            self.phoneName = phoneName
            self.ram = ram
            self.rom = rom


