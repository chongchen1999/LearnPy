class Student:
    company = "SXT"

    @classmethod
    def printCompany(cls):
        print(cls.company)
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school

    @staticmethod
    def printHelp():
        print("Help information")
    
print(type(Student))
Student.printCompany()
Student.printHelp()