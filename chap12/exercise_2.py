#objrball   -- Simulation of Tennis Matches
#           Illustrates design with objects.

from random import random

class Player:
    #A Player keeps track of service probability and score
    def __init__(self, prob):
        #Create a player with this probability
        self.prob = prob
        self.score = 0
        self.game = 0
        self.set = 0
        self.match = 0

    def winsServe(self):
        return random() <= self.prob

    def getProb(self):
        return self.prob

    def incScore(self):
        self.score +=  1
    
    def incGames(self):
        self.game += 1
    
    def incSets(self):
        self.set += 1
    
    def incMatches(self):
        self.match += 1

    def getScore(self):
        return self.score

    def getGame(self):
        return self.game
    
    def getSet(self):
        return self.set
    
    def getMatch(self):
        return self.match


class TennisMatch:
    #A TennisMatch represents a match in progress. A match has two players
    #and keeps track of which one is currently serving
    def __init__(self,  probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA #Player A always serves first
    
    def playGame(self):
        #Play the game to completion
        y = self.playerA.getProb()
        while not self.isOverGame():
            x = random()
            if x < y:
                self.playerA.incScore()
            else:
                self.playerB.incScore()
        
    def isOverGame(self):
        #Returns game is finished (i.e. one of the players has won).
        a, b = self.getScores()
        if ((a >= 4) or (b >= 4)) and abs(a - b) >= 2:
            if a > b:
                self.playerA.incGames()
            else:
                self.playerB.incGames()
            return True
        else:
            return False    
    
    def playSet(self):
        self.playGame()
        a, b = self.getGames()
        while not self.isOverSet():
            if a > b:
                self.playerA.incSets()
            else:
                self.playerB.incSets()

    def isOverSet(self):
        a, b = self.getSets()
        return (
            a != 7
            and b != 7
            and (a >= 6 or b >= 6)
            and abs(a - b) >= 2
            or a == 7
            or b == 7
        )

    def playMatch(self):
        self.playSet() 
        a, b = self.getSets()
        while not self.isOverMatch():
            if a > b:
                self.playerA.incMatches()
            else:
                self.playerB.incMatches()

    def isOverMatch(self):
        a, b = self.getMatches()
        return a > 3 or b > 3

    def changeServer(self):
        self.server = self.playerB if self.server == self.playerA else self.playerA
    
    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()
    
    def getGames(self):
        return self.playerA.getGame(), self.playerB.getGame()

    def getSets(self):
        return self.playerA.getSet(), self.playerB.getSet()

    def getMatches(self):
        return self.playerA.getMatch(), self.playerB.getMatch()

class SimStats:
    #SimStats handles accumulation of statistics across multiple
    #   (completed) matches. This version tracks the wins for each player.
    def __init__(self):
        self.winsA = 0 
        self.winsB = 0

    def update(self, aMatch):
        a, b = aMatch.getMatches()
        if a > b:
            self.winsA +=  1
        else:
            self.winsB += 1
    
    def printReport(self):
        n = self.winsA + self.winsB
        print("Summary of", n, "matches:\n")
        print("         wins (% total)")
        print("---------------------------")
        self.printLine("A", self.winsA, n)
        self.printLine("B", self.winsB, n)

    def printLine(self, label, wins, n):
        template = "Player {0}:{1:5}    ({2:5.1%})"
        print(template.format(label, wins, float(wins)/n))

def printIntro():
    print("This program simulates matches of tennis between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point on the serve.")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many matches to simulate? "))
    return a, b, n

def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for _ in range(n):
        theGame = TennisMatch(probA, probB) #create a new game
        theGame.playMatch()                    #Play it
        stats.update(theGame)             #Extract info

    stats.printReport()

main()
