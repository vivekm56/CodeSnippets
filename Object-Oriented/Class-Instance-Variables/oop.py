class Employee:
    
    numOfEmployees = 0                                  #class-variables shared by all instances
    raiseAmount = 1.04

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName                      #instance-variables unique to all instances
        self.lastName = lastName
        self.salary = salary
        self.mailId = (firstName + lastName + '@company.com').lower()

        Employee.numOfEmployees += 1

    def increment(self):
        self.salary = int(self.salary * self.raiseAmount) #'self.raiseAmount' can be changed by 'Employee.raiseAmount',
                                                          # if you want to keep value unchangeable

emp_1 = Employee('Mark', 'Bucher', 50000)
emp_2 = Employee('Eddiee', 'Paul', 60000)


print(Employee.numOfEmployees)
print(emp_1.raiseAmount)
emp_1.increment()
print(emp_1.salary)
