class Employee:
   
    num_of_emps =0 
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emps += 1        

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('Julita','Inca',5000)
emp_2 = Employee('Ana','Garcia',6000)
emp_3 = Employee('Test','User', 7000)

emp_3.set_raise_amt(1.05)

print(emp_3.raise_amt)    # affects emp_2 AND emp_3 because affect all Employees
print(emp_2.raise_amt)
 
