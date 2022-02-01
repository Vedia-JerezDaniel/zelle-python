#gpa.py
#   Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    filename = input("Enter the name of the grade file: ")
    with open(filename, 'r') as infile:
        #set best to the record for the first student in the file
        best = makeStudent(infile.readline())
        #process subsequent lines of the file
        for line in infile:
            s = makeStudent(line)
            #if this student is best so far, remember it.
            if s.gpa() > best.gpa():
                best = s
    #print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())   

if __name__ == '__main__':
    main()

main()