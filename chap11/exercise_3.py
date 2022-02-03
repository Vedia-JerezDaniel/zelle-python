from gpa import Student

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    with open(filename, 'r') as infile:
        students = [makeStudent(line) for line in infile]
    return students

def writeStudents(students, filename):
    with open(filename, 'w') as outfile:
        for s in students:
            print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)

def main():
    print("This program sorts student grade information by GPA, name, or credits.")
    filename = input("Enter the name of the data file: ")
    # filename = 'gpa1.txt'
    data = readStudents(filename)
    
    while True:
        x = (input('Type "GPA", "name", or "credits" >>>  '))
        m = (input('Type "A" for ascending, "D" for descending.'))

        if x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            if m == "D":
                data.reverse()
            break
        elif x == 'name': 
            data.sort(key=Student.getName)
            s = "_(name)"
            if m == "D":
                data.reverse()
            break 
        elif x == 'credits':
            data.sort(key=Student.getQPoints)
            s = "_(credits)"
            if m == "D":
                data.reverse()
            break
        else:
            print("Please try again.")
        
    #filename = input("enter a name for the outputfile: ")
    filename = "gpa" + s + ".txt"
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()

main()

