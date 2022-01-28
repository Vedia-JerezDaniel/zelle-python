from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, n)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a team winning the serve.")
    print("Starting serve alternates each game. Players win the serve with")
    print("a winning volley, and can score on either teams serve per Rally rules.")

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
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
    return (a > 25 or b > 25) and abs(a-b) >= 2

def printSummary(winsA, winsB, n):
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()

main()
