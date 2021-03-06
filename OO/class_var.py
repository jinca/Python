class Employee:
   
    num_of_emps =0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emps += 1        

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Julita','Inca',5000)
emp_2 = Employee('Ana','Garcia',6000)
emp_3 = Employee('Test','User', 7000)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.email)
print(emp_1.raise_amount)
 
print(emp_2.fullname())
print(emp_2.email)
print(emp_2.pay)

emp_3.raise_amount = 2.0    # only affects emp_3, it can be Employee.raise_amount = 2.0
print(Employee.fullname(emp_3))
print(emp_3.email)
emp_3.apply_raise()
print(emp_3.pay)
 
print('Num of emps: ',Employee.num_of_emps)
print(Employee.__dict__)
