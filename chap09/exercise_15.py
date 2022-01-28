#Suppose you are located at the center of a cube. If you could look all around
#you in every direction, each wall of the cube would occupy 1/6 of your field of
#vision. Suppose you move toward one of the walls so that you are now half-way
#between it and the center of the cube.
#What fraction of your field of vision is now taken up by the closest wall?
#This program uses a Monte Carlo simulation that repeatedly "looks" in a random
#direction and counts how many times it sees the wall

#each wall takes up 60 degrees of vision from the center of the cube
#1/6 is approximately 16.67%
import math
from random import random
from graphics import *

def main():
    n = eval(input("How many steps close to the wall? "))
    prob1 = percentWall(n)
    num, den = percFraction(prob1)
    printSummary(num, den, prob1)

def percentWall(n):
    wall1 = 0
    for _ in range (n):
        if simOneLook() is True:
            wall1 += 1
        else:
            wall1 = wall1
    return wall1 / n

def simOneLook():
    x = 0
    y = 0
    angle = random() * 2 * math.pi
    #travel to wall and stop
    while (abs(x) <= 10) and (abs(y) <= 10):
        x += math.cos(angle)
        y += math.sin(angle)
    return x >= 10

def percFraction(prob1):
    x = round(prob1, 2) * 10
    m = 10
    n = x
    while m != 0:
        y = m
        m = n % m
        n = y
    num = x / n
    den = 10 / n

    return num, den


def printSummary(num, den, prob1):
    print("The closest wall occupies {0}/{1} of your vision, or {2:0.1%}.".format(int(num), int(den), prob1))

if __name__ == '__main__': main()


main()