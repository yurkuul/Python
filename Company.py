class Employee():
    name = ""
    empNum = 0
    salary = 0.0
    projects = list()
    def __init__(self, theName, num, sal):
        self.name = theName
        self.empNum = num
        self.salary = sal
    
    def addProject(self, aProject):
        self.projects.append(aProject)
    
    def __str__(self):
        return "{}, employee number: {}, with a salary of ${:.2f}. Current projects: {}".format(self.name, self.empNum, self.salary, self.projects)
    
    def getName(self):
        return self.name
    
    def getNum(self):
        return self.empNum
    
    def getSalary(self):
        return self.salary
    
    def setName(self, theName):
        self.name = theName
    
    def setNum(self, num):
        self.empNum = num
        
    def setSalary(self, sal):
        self.salary = sal
