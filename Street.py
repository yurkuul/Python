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
