class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Julita','Inca',5000)
emp_2 = Employee('Ana','Garcia',6000)
emp_3 = Employee('Test','User', 7000)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.email)

print(emp_2.fullname())
print(emp_2.email)

print(Employee.fullname(emp_3))
print(emp_3.email)
