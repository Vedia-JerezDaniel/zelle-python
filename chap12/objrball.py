#objrball   -- Simulation of a racquet game
#           Illustrates design with objects.
from random import random

class Player:
    #A Player keeps track of service probability and score
    def __init__(self, prob):
        #Create a player with this probability
        self.prob = prob
        self.score = 0

    def winsServe(self):
        return random() <= self.prob

    def incScore(self):
        self.score = self.score + 1

    def getScore(self):
        return self.score


class RBallGame:
    #A RBallGame represents a game in progress. A game has two players
    #and keeps track of which one is currently serving
    def __init__(self,  probA, probB):
        #Create a new game having players with the given probs.
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA #Player A always serves first
    
    def play(self):
        #Play the game to completion
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()
        
    def isOver(self):
        #Returns game is finished (i.e. one of the players has won).
        a, b = self.getScores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)

    def changeServer(self):
        #Switch which player is serving
        self.server = self.playerB if self.server == self.playerA else self.playerA
    
    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

class SimStats:
    #SimStats handles accumulation of statistics across multiple
    #   (completed) games. This version tracks the wins and shutouts for  each player.
    def __init__(self):
        self.winsA = 0 
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA += 1
            if b == 0:
                self.shutsA += 1
        else:
            self.winsB += 1
            if a == 0:
                self.shutsB += 1
    
    def printReport(self):
        n = self.winsA + self.winsB
        print("Summary of", n, "games:\n")
        print("         wins (% total)  shutouts (% wins)   ")
        print("----------------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)

    def printLine(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}    ({2:5.1%})  {3:6}  ({4})"
        shutStr = "-----" if wins == 0 else "{0:4.1%}".format(float(shuts)/wins)
        print(template.format(label, wins, float(wins)/n, shuts, shutStr))

def printIntro():
    print("This program simulates games of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve. \n")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def main():
    printIntro()

    probA, probB, n = getInputs()
    #Play the games
    stats = SimStats()
    for _ in range(n):
        theGame = RBallGame(probA, probB) #create a new game
        theGame.play()                    #Play it
        stats.update(theGame)             #Extract info

    #Print the results
    stats.printReport()

main()
