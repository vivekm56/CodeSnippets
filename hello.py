class Student:
# create a constructor or initializer to store value by itself
    def __init__(self, sFirstName, sLastName, sClass, sRollNo):
        self.sFirstName = sFirstName
        self.sLastName = sLastName
        self.sClass = sClass
        self.sRollNo = sRollNo
 
    def studentId(self):
        studentId = self.sFirstName + self.sLastName + self.sRollNo +'@university.com'
        return studentId.lower()

s_1 = Student('Bob', 'Straus', '10', '12')
s_2 = Student('Stuart', 'lee', '11', '35')

print(s_1.studentId())
print(Student.studentId(s_2))