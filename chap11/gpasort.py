from gpa import *

def readStudents(filename):
    with open(filename, 'r') as infile:
        students = [makeStudent(line) for line in infile]
    return students

def writeStudents(students, filename):
    with open(filename, 'w') as outfile:
        for s in students:
            print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(key=Student.gpa)
    filename = input("enter a name for the outputfile: ")
    writeStudents(data, filename)
    print("the data has been written to", filename)

if __name__ == '__main__': main()



