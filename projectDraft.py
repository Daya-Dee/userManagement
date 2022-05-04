class person:
    def __init__(self, name, age, bday) -> None:
        self.name = name

class student(person):
    def __init__(self, name, age, bday) -> None:
        super().__init__(self, name, age, bday)
    
class Employee:
    userType = "Employee"
    
    employeeIDs = []
    employeeFirstName = []
    employeeLastName = []
    employeeBirthday = []
    employeePosition = []
    employeeWorkPlace = []
    
class Other:
    userType = "Other"
    
    otherIDs = []
    otherFirstName = []
    otherLastName = []
    otherBirthday = []
    otherRole = []
    
class MainUser:
    userType = "Main User"
    
    mainID = []
    mainFirstName = []
    mainLastName = []
    mainBirthday = []
    mainRole = []