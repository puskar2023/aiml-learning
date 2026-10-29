'''Given a list of tuples with info(name, subject):
list all unique course
list students enrolled in English
create dictionary (student, set of courses)
'''

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
# First and second part

list_course = set()
list_student = set()
for name, course in info:
    list_course.add(course)
    list_student.add(name)
    if (course == "English") :
        print(name)
    
print(list_course)
print(list_student)


# Third part
dict = {}
for name, course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
        
print(dict)