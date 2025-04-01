class Employee:
    __HRA = 400
    __DA = 200
    __TAX = 0.05

    def __init__(self, empID, empName, dept, salary):
        self.empID = empID
        self.empName = empName
        self.dept = dept
        self.salary = salary

    def displayDetails(self):
        print("\t Employee Details\n")
        print("Employee ID: ", self.empID)
        print("Employee Name: ", self.empName)
        print("Employee Department: ", self.dept)
        print("Employee Salary: ", self.salary)

    def calculateSalary(self):
        print("\n\t Salary Details\n")

        gross_salary = self.salary + Employee.__HRA + Employee.__DA
        tax_deduction = Employee.__TAX * gross_salary
        final_salary = gross_salary - tax_deduction
        print(f"Gross Salary: {gross_salary}")
        print(f"Tax Deduction (5%): {tax_deduction}")
        print(f"Final Salary: {final_salary:.2f}")

totalEmp = int(input("Enter total employees: "))

for i in range(totalEmp):
    print("\n\tEnter Employee", i + 1, "Details\n")
    empID = int(input("Enter Employee ID: "))
    empName = input("Enter Employee Name: ")
    dept = input("Enter employee department: ")
    salary = float(input("Enter salary of the employee: "))
    employee1 = Employee(empID, empName, dept, salary)

    employee1.displayDetails()
    employee1.calculateSalary()

