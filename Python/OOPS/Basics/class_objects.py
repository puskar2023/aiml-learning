class Student:
    subject = "Python" #class attribute
    
    def __init__(self, name, cgpa):
        self.name = name #instance attribute
        self.cgpa = cgpa
        
    def get_cgpa(self):  #instance method
        return self.cgpa
    
stu1 = Student("Alice", 9.0)
stu2 = Student("Bob", 9.1)
stu3 = Student("Sarthak", 9.3)

print(f"{stu3.name} has cgpa = {stu3.get_cgpa()}")
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa = {stu2.get_cgpa()}")