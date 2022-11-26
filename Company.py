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

class Project():
    title = ""
    budget = 0.0
    dueDate = ""
    employees = list()
    def __init__(self, theTitle, money, deadline):
        self.title = theTitle
        self.budget = money
        self.dueDate = deadline
    
    def addTeamMember(self, anEmployee):
        self.employees.append(anEmployee)
    
    def __str__(self):
        return "Project title: {}, with a budget of ${:.2f}, due {}. Employees working on this project: {}".format(self.title, self.budget, self.dueDate, self.employees)
        
    def getTitle(self):
        return self.title
    
    def getBudget(self):
        return self.budget
    
    def getDueDate(self):
        return self.dueDate
    
    def setBudget(self, money):
        self.budget = money
        
    def setDueDate(self, deadline):
        self.dueDate = deadline    
