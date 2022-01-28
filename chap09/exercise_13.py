#One-dimensional random walk
import random
import math

def main():
    printIntro()
    n = eval(input("How many steps do you intend to take per trip? "))
    avgDist = avgTravel(n)
    printSummary(avgDist)

def printIntro():
    print("This program simulates a random walk in two dimensions, where the")
    print("object will move either forward or backward, left of right at random.")
    print('Varialble "n" represents the number of random steps per trip. The program')
    print("will simulate 1000 trips by default, and will return the average")
    print("distance 'as the crow flies' traveled per trip.")

def avgTravel(n):
    totBlocks = 0
    avgDist = 0
    for _ in range (n):
        avgBlocks = simNBlocks(n)
        totBlocks += avgBlocks
    avgDist = 0 if totBlocks == 0 else totBlocks / n
    return avgDist

def simNBlocks(n):
    blocksX = blocksY = 0
    for _ in range (n):
        x = 4 * random.random()
        if 0 <= x < 1:
            blocksX +=  1
        elif 1 <= x < 2:
            blocksX -= 1
        elif 2 <= x < 3:
            blocksY +=  1
        else:
            blocksY -= 1

    return math.sqrt((blocksX ** 2 + blocksY ** 2))

def printSummary(avgDist):
    print("The object will travel an average of {0:0.2f} blocks based on the simulation.".format(avgDist))

if __name__ == '__main__': main()

main()
