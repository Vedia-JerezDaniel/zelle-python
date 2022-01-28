from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    matchA, matchB, shutA, shutB = simNMatches(n, probA, probB)
    printSummary(matchA, matchB, shutA, shutB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a player winning the serve.")
    print("Starting serve alternates each game, but Player A starts each match.")
    print()

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNMatches(n, probA, probB):
    #Simulates n Matches of racquetball between players whos
    matchA = matchB = 0
    shutA = shutB = 0
    
    for _ in range(n):
        winsA, winsB, shutA, shutB = simOneMatch(probA, probB, shutA, shutB)
        if winsA > winsB: matchA += 1
        else: matchB += 1
    return matchA, matchB, shutA, shutB

def simOneMatch(probA, probB, shutA, shutB):
    winsA = winsB = 0
    x = 1
    while winsA !=2 and winsB !=2:
        scoreA, scoreB, shutA, shutB = simOneGame(probA, probB, x, shutA, shutB)
        if scoreA > scoreB:   winsA += 1
        else:   winsB += 1
        x += 1
    return winsA, winsB, shutA, shutB

def simOneGame(probA, probB, x, shutA, shutB):
    serving = findService(x)
    scoreA = 0
    scoreB = 0

    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:  serving = "B"
        elif serving == "B":
            if random() < probB:
                scoreB += 1
            else:  serving = "A"
    if scoreA == 7:  shutA += 1
    if scoreB == 7:  shutB += 1
    return scoreA, scoreB, shutA, shutB

def findService(x):
    return "A" if x % 2 == 0 else "B"

def gameOver(a, b):
    if a == 0 and b == 7:
        return b == 7
    elif b == 0 and a == 7:
        return a == 7
    elif abs(a-b) >= 2:
        return True
    else:
        return False

def printSummary(matchA, matchB, shutA, shutB):
    n = matchA + matchB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(matchA, matchA/n))
    print("Wins for B: {0} ({1:0.1%})".format(matchB, matchB/n))
    print()
    print("Shutouts for A: {0} ({1:0.1%})".format(shutA, shutA/matchA))
    print("Shutouts for B: {0} ({1:0.1%})".format(shutB, shutB/matchB))


main()
