class Employee:
    def __init__(self, eid, ename):
        self.ename = ename
        self.eid = eid

    def display(self):
        print("Employee ID: ", self.eid)
        print("Employee Name: ", self.ename)

class Salary(Employee):
    def __init__(self, eid, ename, salary):
        super().__init__(eid, ename)
        self.salary = salary

    def salary_display(self):
        print("Name of the employee: ", self.ename)
        print("Id of the employee: ", self.eid)
        print("Salary of the employee: ", self.salary)

emp = Salary(101, "Ashwin", 50000)
emp.display()
print("\n")
emp.salary_display()