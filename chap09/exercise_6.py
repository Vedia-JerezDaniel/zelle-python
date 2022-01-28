#Tennis Scoring
#Love, 15, 30, 40, game, win by 2
#Set is best of 6, win by 2
#Match is best of 5
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNMatches(n, probA, probB)
    printSummary(winsA, winsB, n)

def printIntro():
    print("This program simulates a series of tennis matches between player")
    print('"A" and player "B". The abilities of each player are')
    print("represented by percentage chance of winning a volley. The")
    print("percentages add up to 100.")
    print()
    print("Game")
    print("As in real tennis, each game is played through 4 points")
    print("(Love, 15, 30, 40, game) where the player must win by two.")
    print("Players can score on either serve.")
    print()
    print("Set")
    print("A set is won when a player reaches 6 victorious games, and has a")
    print("lead of two. If for example, sets reach 6-5, the players will play")
    print("another round. If the score reaches 6-6, there will be a")
    print("tiebreaking game.")
    print()
    print("Match")
    print("A Match is won when a player reaches his/her 3rd victorious set.")
    print("No winning by two, no tie-breaker, for the purposes of this simulation")
    print()


def getInputs():
    probA = eval(input("What is the percent prob. player A wins a volley? "))
    probA = probA / 100
    probB = 1 - probA
    n = eval(input("How many games to simulate? "))
    return probA, probB, n

def simNMatches(n, probA, probB):
    winsA = winsB = 0
    for _ in range(n):
        matchA, matchB = simOneMatch(probA, probB)
        if matchA > matchB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneMatch(probA, probB):
    matchA = matchB = 0
    while not matchOver(matchA, matchB):
        setA, setB = simOneSet(probA, probB)
        if setA > setB:    matchA += 1
        else:  matchB += 1
    return matchA, matchB

def matchOver(a, b):
    return a > 3 or b > 3

def simOneSet(probA, probB):
    scoreA, scoreB = simOneGame(probA, probB)
    setA = setB = 0
    while not setOver(setA, setB):
        if scoreA > scoreB:     setA +=  1
        else:       setB +=  1
    return setA, setB

def setOver(a, b):
    return (
        a != 7
        and b != 7
        and (a >= 6 or b >= 6)
        and abs(a - b) >= 2
        or a == 7
        or b == 7
    )

def simOneGame(probA, probB):
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if random() < probA:
            scoreA += 1
        else:         scoreB +=  1
    return scoreA, scoreB


def gameOver(a, b):
    return (a >= 4 or b >= 4) and abs(a-b) >=2

def printSummary(winsA, winsB, n):
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()

main()