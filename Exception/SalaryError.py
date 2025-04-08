class SalaryError(Exception):
    def __init__(self,salary,message="salary not in range between 10000 to 50000"):
        self.salary = salary
        self.msg = message
        super().__init__(self.msg)

salary = int(input('Enter salary '))
if not 10000 < salary < 50000:
    raise SalaryError(salary)
