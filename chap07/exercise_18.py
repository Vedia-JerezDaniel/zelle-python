def leapYear(year):
    if (year % 4) != 0:
        return False
    else:
        return (year % 100) == 0 and (year % 400) ==0 or year % 100 != 0

def main():
    try:
        dateStr = input("Please enter a date in form 00/00/0000: ")

        monthStr, dayStr, yearStr = dateStr.split("/")
        month = int(monthStr)
        day = int(dayStr)
        year = int(yearStr)

        if month > 12 or day > 31:
            print("This date is invalid.")
        elif day <= 28:
            print("This date is valid.")
        elif month == 2 and day == 29:
            if leapYear(year) == False:
                print("This date is invalid.")
            else:
                print("This date is valid.")
        elif month in {1, 3, 5, 7, 8, 10, 12} and day == 31:
            print("This date is valid")
        else:
            print("The date is invalid.")

    except ValueError:
        print("Your input was not in the correct form.")
    except:
        print("Something went wrong!")
        
        
main()
