#One-dimensional random walk
import random

def main():
    printIntro()
    n = eval(input("How many steps do you intend to take? "))
    avgTravel = avgSteps(n)
    print("The object will travel an average of", avgTravel, "based on the simulation.")

def printIntro():
    print("This program simulates a random walk in one dimension, where the")
    print("object will move either forward or backward at random. Varialble")
    print('"n" represents the number of random steps per trip. The program')
    print("will simulate 1000 trips by default, and will return the average")
    print("distance traveled per trip.")

def avgSteps(n):
    totTravel = 0
    for _ in range (n):
        steps = simNSteps(n)
        totTravel += steps
    return 0 if totTravel == 0 else totTravel / n

def simNSteps(n):
    steps = 0
    for _ in range (n):
        x = random.randint(0,1)
        if x == 1:      steps += 1
        elif x == 0:    steps -= 1
        else:           steps = steps
    return steps


if __name__ == '__main__': main()

main()