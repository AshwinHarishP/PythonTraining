def displayDetails(details):
    print("--------Employee Details--------\n")
    
    for name, salary, final_salary in details:
        print("Name of the employee: " + name)
        print("Yearly salary of employee before tax: ", salary * 12, "LPA")
        print("Monthly salary of employee before tax: ", salary)
        print("\n")

        print("Yearly salary of the employee after tax: ", final_salary * 12, "LPA") 
        print("Monthly salary of the employee after tax: ", final_salary)
        print("\n")


def salaryCalculation(salary):
    lpa = salary * 12 
    tax_deduction = 0  

    if 500000 <= lpa < 800000:
        tax_deduction = 0.10 

    elif lpa >= 800000:
        tax_deduction = 0.10 + 0.20  

    salary_after_tax = salary - (salary * tax_deduction)  
    return salary_after_tax 
    

def addEmployeeInfo(no_of_employee):
    details = []  
    global employeeSalary
    for i in range(no_of_employee):
        print("--------Enter Details of Employee", i+1, "--------")
        employee_name = input("Enter Name of the Employee: ")
        namesOfemployee.append(employee_name)
        
        employee_salary = int(input("Enter Monthly Salary: "))
        employeeSalary += (employee_salary,)

        final_salary = salaryCalculation(employee_salary)  
        details.append((employee_name, employee_salary, final_salary))  
    return details


print("-------- Employee App --------")
namesOfemployee = list()
employeeSalary = tuple()

no_of_employee = int(input("Enter Total Number of Employees: "))
details = addEmployeeInfo(no_of_employee)
displayDetails(details)
