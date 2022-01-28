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
    print("a winning volley, and can score only on their own serve.")
    
def getInputs():
    a = eval(input("What is the prob. Team A wins a serve? "))
    b = eval(input("What is the prob. Team B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    for _ in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB: winsA +=  1
        else: winsB +=  1
    return winsA, winsB

def simOneGame(probA, probB, n):
    # serving = findService(n)
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        # if serving == "A":
        if random() < probA: scoreA += 1
        # else: serving = "B"
        # if serving == "B":
        else: 
            scoreB += 1
            # else:  serving = "A"
    return scoreA, scoreB

# def findService(n):
#     return "A" if n % 2 == 0 else "B"

def gameOver(a, b):
    return (a > 15 or b > 15) and abs(a-b) >= 2

def printSummary(winsA, winsB, n):
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))


main()
