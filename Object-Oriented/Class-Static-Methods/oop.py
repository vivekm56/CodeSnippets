class Employee:
    
    numOfEmployees = 0
    raiseAmount = 1.04

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.mailId = (firstName + lastName + '@company.com').lower()

        Employee.numOfEmployees += 1    #knit method

    def increment(self):
        self.salary = int(self.salary * self.raiseAmount) 
        
    @classmethod                        #It can be used as an alternative constructor
    def set_raise_amt(cls, amount):     #It can be called a class instead of an Instance
        cls.raiseAmount = amount

    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, salary = emp_str_1.split('-')
        return (firstName, lastName, salary)

    @staticmethod                       #Normal Method or function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True


emp_1 = Employee('Mark', 'Bucher', 50000)
emp_2 = Employee('Eddiee', 'Paul', 60000)

Employee.set_raise_amt(1.05)
print(emp_1.raiseAmount)
print(emp_2.raiseAmount)
print(Employee.raiseAmount)

# Employee.set_raise_amt(1.06)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


# new_emp_1 = Employee(firstName, lastName, salary)
new_emp_1 = Employee.from_string(emp)

print(new_emp_1.mailId)
print(new_emp_1.salary)

import datetime

my_date = datetime.date(2020,6,17)

print(Employee.is_workday(my_date))
