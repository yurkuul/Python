"""
Question 1a)

Write a class that represents a movie.
   -> A movie has a name(str), length(int), and a list of actors
   -> Write an addActor() method
   -> Write an __str__ method that displays an appropriate output
"""

class Movie():
    def __init__(self, theName, theLength):
        self.name = theName
        self.length = theLength
        self.actors = list()
    
    def addActor(self, actorName):
        self.actors.append(actorName)
    
    def __str__(self):
        output = "{} is {} minutes long.\nThe actors are:\n".format(self.name, self.length)
        for actor in self.actors:
            output += actor + "\n"
        return output
