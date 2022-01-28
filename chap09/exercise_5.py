from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA1, winsB1 = normalVolley(n, probA, probB)
    winsA2, winsB2 = rallyVolley(n, probA, probB)
    printSummary(winsA1, winsB1, winsA2, winsB2, n)

def printIntro():
    print("This program is designed to compare the difference between Normal")
    print("and Rally scoring in a simulation of (n) games of Volleyball")
    print("given a probability (a number between 0 and 1) that reflects the")
    print("likelihood of a team winning the serve.")

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def normalVolley(n, probA, probB):
    winsA = winsB = 0
    for _ in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, n):
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if random() < probA:
            scoreA += 1
        else:        scoreB += 1
        if random() < probB:
            scoreB += 1
        else:        scoreA += 1
    return scoreA, scoreB

def gameOver(a, b):
    return (a > 15 or b > 15) and abs(a-b) >= 2

def rallyVolley(n, probA, probB):
    winsA = winsB = 0
    for _ in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def gameOver(a, b):
    return (a > 25 or b > 25) and abs(a-b) >= 2

def printSummary(winsA1, winsB1, winsA2, winsB2, n):
    print("\nGames simulated: ", n)
    print("Results for Normal Volleyball to 15, score on own serve.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA1, winsA1/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB1, winsB1/n))
    print()
    print("Results for Rally Volleyball to 25, score on any serve.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA2, winsA2/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB2, winsB2/n))
    print()


    devA = (winsA2/n - winsA1/n)
    devB = (winsB2/n - winsB1/n)
    if (winsA1 > winsB1) and (winsA2 > winsB2):
        if devA > 0:
            print("Team A's advantage was magnified {0:0.1%} in their favor".format(devA))
            print("during the rally scoring match.")
        elif devA < 0:
            print("Team A's advantage was reduced {0:0.1%} in their favor".format(abs(devA)))
            print("during the rally scoring match.")
        else:
            print("The scoring differences were not statistically significant.")
    elif (winsB1 > winsA1) and (winsB2 > winsA2):
        if devB > 0:
            print("Team B's advantage was magnified {0:0.1%} in their favor".format(devB))
            print("during the rally scoring match.")
        elif devB < 0:
            print("Team B's advantage was reduced {0:0.1%} in their favor".format(abs(devB)))
            print("during the rally scoring match.")
        else:
            print("The scoring differences were not statistically significant.")
    else:
        print("Neither team's advantage was statistically significant.")
        print("If the initial probabilities were near equal, it is impossible to")
        print("derive significance from the data.")
        print("Try a larger sample size.")


if __name__ == '__main__': main()

main()