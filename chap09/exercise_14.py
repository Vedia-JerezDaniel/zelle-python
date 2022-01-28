#graphical program to trace random walk in 2 dimensions

import math
from random import random
from graphics import *

def main():
    n = eval(input("How many steps do you intend to take through the simulation? "))
    win = GraphWin("Random Walk", 600, 600)
    win.setCoords(-100, -100, 100, 100)
    for _ in range (5):
        randWalk(n, win)


def randWalk(n, win):
    point2 = Point(0,0)
    for _ in range (n):
        x = point2.getX()
        y = point2.getY()

        point1 = simOneStep(x, y)
        point1.draw(win)
        line = Line(point2, point1)
        line.draw(win)
        point2 = point1

def simOneStep(x, y):
    angle = random() * 2 * math.pi
    x = x + math.cos(angle)
    y = y + math.sin(angle)
    return Point(x, y)

if __name__ == '__main__': main()

main()
