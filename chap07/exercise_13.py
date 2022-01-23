def leapYear(year):
    if (year % 4) != 0:
        return False
    else:
        return (year % 100) == 0 and (year % 400) ==0 or year % 100 != 0

def verDate(month, day, year):
    if month > 12 or day > 31:
        return False
    else:
        return (
            day <= 28 or month != 2 or day != 29 or leapYear(year) != False
        ) and (day <= 28 or month == 2 and day == 29 or day != 31)
        
def main():
    dateStr = input("Enter a date as '6/29/1100': ")
    monthStr, dayStr, yearStr = dateStr.split("/")
    month = int(monthStr)
    day = int(dayStr)
    year = int(yearStr)

    if verDate(month, day, year) == False:
        print("This date is invalid.")
    else:
        dayNum = 31 * (month - 1) + day
        if month > 2:
            if leapYear(year) == True:
                dayNum = dayNum - (4 * (month) + 23)//10 + 1
            else:
                dayNum = dayNum - (4 * (month) + 23)//10
        else:
            dayNum = 31 * (month - 1) + day
    print("The numeric value of this date is {}.".format(dayNum))

main()
