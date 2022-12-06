class Street():
    def __init__(self, theName:str, theLength:int, numCars:int, theCondition:str):
        self.name = theName #name of street
        self.length = theLength #in km
        self.carsTravelled = numCars #cars travelled per 
        self.condition = theCondition #condition of the street ('poor', 'fair', 'good')
    
    def getName(self):
        """
        Returns the name of the street.
        """
        return self.name

    def getLength(self):
        """
        Returns the length of the street.
        """
        return self.length
    
    def getCarsTravelled(self):
        """
        Returns the number of cars travelled on the street.
        """
        return self.carsTravelled
    
    def getCondition(self):
        """
        Returns the condition of the street.
        """
        return self.condition

    def compare(self, otherStreet):
        """
        Compares the street that calls this method with a second street.

        Return True if the first street is in need of urgent repair compared to
        the second street.
        """
        firstRepair = True
        if (self.condition == "good" and otherStreet.getCondition() != "good"):
            firstRepair = False
        elif (self.condition == "fair" and otherStreet.getCondition() == "poor"):
            firstRepair = False
        elif (self.condition == otherStreet.getCondition()):
            if (self.getCarsTravelled() < otherStreet.getCarsTravelled()):
                firstRepair = False
        return firstRepair
    
    def __str__(self):
        return "{} is {} km long, sees {} cars per day and is in {} condition.".format(
            self.name, self.length, self.carsTravelled, self.condition)
