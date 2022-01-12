def main():
    #get the date
    dateStr = input("Enter a date (mm/dd/yyy): ")

    monthStr, dayStr, yearStr = dateStr.split("/")

    #convert monthStr to the month name
    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    print("The converted date is:", monthStr, dayStr+",", yearStr)

main()
