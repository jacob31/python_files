# file name: leap_year.py 
# by: Ben Silbernagel
# date: 6/15/2016
# class: Intro to Computer Science, by Udacity
# purpose: functions dealing with leap year

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def is_leap_baby(day,month,year):
    if leap_year(year):
        if month == 2:
            if day == 29:
                return True
            else:
                return False
        else:
            return False
    else:
        return False