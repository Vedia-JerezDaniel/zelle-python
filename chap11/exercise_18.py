#One-dimensional random walk (log blocks traveled)
from random import random

def avgSteps(n):
    totTravel = 0
    for _ in range (10):
        steps = simNSteps(n)
        totTravel += steps
    return 0 if totTravel == 0 else totTravel / 10

def simNSteps(n):
    steps = 0
    for _ in range (n):
        x = 2 * random() - 1
        if x > 0:
            steps += 1
        elif x < 0:
            steps -= 1
        else:
            steps = steps
    return steps

def printIntro():
    print("This program simulates a random walk in one dimension, where the")
    print("object will move either forward or backward at random. Variable")
    print('"n" represents the number squares on the block. The program')
    print("will return how many times each square is stepped on.")

def main():
    printIntro()
    n = eval(input("How many squares are on the sidewalk?"))
    squares = [0 for _ in range(n + 1)]
    steps = int(n / 2)
    while 0 < steps < n:
        x = 2 * random() - 1
        if x > 0:
            steps += 1
            squares[steps] = squares[steps] + 1
        elif x < 0:
            steps -= 1
            squares[steps] = squares[steps] + 1
        else:
            steps = steps
    for i in range(len(squares)-1):
        print("Square {0}: {1}".format(i + 1,squares[i]))


main()

