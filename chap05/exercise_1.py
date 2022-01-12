def main():
    #get the date
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))

    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    monthstr = months[month-1]
    print("The converted date is {1}/{0}/{2}, or {3} {0} {2}".format(day, month, year, monthstr))

    
main()


# printfile.py
# Prints a file to the screen.
def main():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
    for line in infile:
        print(line,end="")
    # data = infile.read()
    # print(data)
main()
