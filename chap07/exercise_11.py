#if year is divisible by 4, it's a leap years
#unless it's a century year not divisible by 400
#leap year yes or no

def leapYear(year):
    if (year % 4) != 0:
        print("{} is not a leap year.".format(year))
    elif (year % 100) == 0 and (year % 400) == 0 or year % 100 != 0:
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))


leapYear(1981)