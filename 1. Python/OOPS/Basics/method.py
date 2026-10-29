class Student:
    subject = "Python"
    
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        
    @classmethod
    def get_subject(cls):  #class method
        print(f"subject is {cls.subject}")
        
    def get_info(self):   #instance method
        print(f"{self.name} has {self.cgpa} cgpa and {self.subject} subject")
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Final price is {final_price}")
    
stu1 = Student("Alice", 9.0)
stu2 = Student("Bob", 9.1)
stu3 = Student("Sarthak", 9.3)

stu1.get_info()
stu1.get_subject()
Student.get_subject()
stu1.calc_discount(6500, 10)