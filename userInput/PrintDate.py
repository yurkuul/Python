daysOfWeek = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday",
              6:"Friday", 7:"Saturday"}
months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 
          7:"July", 8:"August", 9:"September", 10:"October", 11:"November",
          12:"December"}

def checkDayName():
    while (True):
        theDay = input("Please enter the weekday/weekend name as an integer: ")
        if (not theDay.isnumeric()):
            print("That is not an integer!")
        elif (int(theDay) < 1 or int(theDay) > 7):
            print("That is not a valid day.")
        else:
            return int(theDay)

def checkMonth():
    while (True):
        month = input("Please enter a month: ")
        if (not month.isnumeric()):
            print("That is not an integer!")
        elif (int(month) < 1 or int(month) > 12):
            print("That is not a valid month.")
        else:
            return int(month)
