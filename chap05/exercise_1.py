def main():
    #get the date
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))

    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    monthstr = months[month-1]
    print("The converted date is {1}/{0}/{2}, or {3} {0} {2}".format(day, month, year, monthstr))


    
main()
