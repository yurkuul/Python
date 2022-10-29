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

def checkDay():
    checkValid = False
    while (True):
        day = input("Please enter today's date: ")
        if (not day.isnumeric()):
            print("That is not a number!")
        elif (int(day) <= 0):
            print("That is not a valid day.")
        elif (month in [1, 3, 5, 7, 8, 10, 12]):
            if (int(day) > 31):
                print("That is out of range for your month.")
            else:
                checkValid = True
        elif (month in [4, 6, 9, 11]):
            if (int(day) > 30):
                print("That is out of range for your month.")
            else:
                checkValid = True
        elif (month == 2):
            if (int(day) > 28):
                print("That is out of range for your month.")
            else:
                checkValid = True
        if (checkValid):
            return int(day)

def checkYear():
    while (True):
        year = input("Please enter a year: ")
        if (not year.isnumeric()):
            print("That is not a year!")
        elif (int(year) < 1000 or int(year) > 2022):
            print("That year is out of range.")
        else:
            return int(year)

theWeekDay = checkDayName()
print()
month = checkMonth()
print()
day = checkDay()
print()
year = checkYear()
print()

theWeekDay = daysOfWeek[theWeekDay]
theMonth = months[month]

print("The date is {}, {} {}, {}.".format(theWeekDay, theMonth, day, year))
