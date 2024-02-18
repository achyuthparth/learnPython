class Person:
    name: str
    email: str
    def __init__(self, name = "", email = ""):
        self.name = name
        self.email = email
    
    def __init__(self, name):
        self.name = name
        self.email = "dummy"

class Student(Person):
    grades: dict
    classes: list
    def __init__(self, name = "", email = "", grades = {}):
        super().__init__(self, name, email)
        #self.

class Teacher(Person):
    subject: str

class PrivateTeacher(Teacher):
    students: list

class PublicTeacher(Teacher):
    school: str
    
class TA(Teacher, Student):
    pass