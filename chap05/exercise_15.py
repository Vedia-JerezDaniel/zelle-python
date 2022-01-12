#This program plots student exam scores on a horizontal bar chart
#open student_test.txt
from graphics import *
def main():
    fname = input("Enter filename: ")
    with open(fname, "r") as infile:
        numStud = int(infile.readline())
        studName = []
        grade = []
        for line in infile.readlines():
            x, y = line.split(": ")
            y = y[:-1]
            studName.append(x)
            grade.append(y)

        print(studName)
        print(grade)
#initialize graphWin of size 400, (100 x numStud)
        win = GraphWin("Student Grade Chart", 400, 50 * numStud)
        win.setCoords(-30, (10 * numStud + 2), 120, 0)
        #draw text studName
        for i in range (numStud):
            s = studName[i].rjust(10)
            Text(Point(-20, 15 + numStud * .8 * i), s).draw(win)
        #draw Rectangle and clone
        for i in range (numStud):
            r = Rectangle(Point(0, 13 + numStud * .8 *i), Point(grade[i], 17 + numStud * .8 * i))
            r.draw(win)
main()
