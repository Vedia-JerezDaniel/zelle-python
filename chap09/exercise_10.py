#n is number of darts thrown
from graphics import *
from random import random

def main():
    printIntro()
    n = eval(input("Iterations: "))
    hits = simDarts(n)
    pi = getPi(hits, n)
    printSummary(pi)

def printIntro():
    print("This program is designed to estimate the value of pi using a")
    print("simulation of darts, where the dart board is nested inside a.")
    print("square cabinet with lengths equal to the diameter of the board.")
    print("Enter the number of iterations you would like the simulation to")
    print("perform. Note: the higher the number, the more precise the results.")
    print("Enter a number greater than 500.")

def simDarts(n):
    win = GraphWin("", 400, 400)
    win.setCoords(-1, -1, 1, 1)

    hits = 0
    for _ in range (n):
        point = getDart()
        if hitBoard(point) is True:
            hits += 1
        else:
            hits = hits
    win.close()
    return hits
    
def getDart():
    x = 2 * random() - 1
    y = 2 * random() - 1
    return Point(x, y)

def hitBoard(point):
    x = point.getX()
    y = point.getY()
    return (x ** 2 + y ** 2) <= 1

def getPi(hits, n):
    return 4 * (hits/n)

def printSummary(pi):
    print("The approximate value of pi based on the simulation is {}.".format(pi))

if __name__ == '__main__': main()
