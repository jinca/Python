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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
  
emp_str_1 = 'Julita-Inca-5000'
emp_str_2 = 'Ana-Garcia-6000'
emp_str_3 = 'Test-User-7000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())    
print(new_emp_1.pay)
