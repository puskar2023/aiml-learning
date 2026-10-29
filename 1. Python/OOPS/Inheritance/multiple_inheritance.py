class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
class Student:
    def __init__(self, gpa):
        self.gpa = gpa
        
class TA(Teacher, Student):
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name
        
ta1 = TA("Sarthak", 25000, 9.3)

print(ta1.name, ta1.salary, ta1.gpa)