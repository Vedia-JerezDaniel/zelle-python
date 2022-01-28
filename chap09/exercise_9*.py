from random import randrange

def main():
     printIntro()
     n = eval(input("Iterations: "))
     for i in range (13):
        i = i + 1
        busts = simNHands(n, i)
        printSummary(busts, n, i)

def printIntro():
    print("This program simulates (n) hands of blackjack for each possible")
    print("starting card and displays the probability of the dealer busting")
    print("for a particular draw.")
    print("Enter the number of iterations you would like the simulation to")
    print("perform. Note: the higher the number, the more precise the results.")
    print("Enter a number greater than 100.")
    
def simNHands(n, startCard):
     print(startCard)
     return sum(not simOneHand(startCard) for _ in range(n))

def simOneHand(startCard):
     x = startCard
     if x in [11, 12, 13]:
          x = 10
     y = simOneCard()
     hand = x + y
     while hand < 17:
          if hasAce(x) is False and hasAce(y) is False:
               z = simOneCard()
               if hasAce(z) is False:
                    hand += z
               else:
                    hand += 11 if 10 >= hand >= 6 else hand + 1
          elif hasAce(x) is True and hasAce(y) is True:
               z = simOneCard()
               if hasAce(z) is False:
                    hand += z
               hand += 11 if 10 >= hand >= 6 else hand + 1
          elif 10 >= hand >= 6:
               hand += 11
          else:
               if hand >= 15:
                    break
               z = simOneCard()
               hand += 1 + z
     return hand <= 21

def simOneCard():
     x = randrange(1, 13)
     if x in [11, 12, 13]:
          x = 10
     return x

def hasAce(x):
     return x == 1

def printSummary(busts, n, i):
    cards = ['1','Ace', '2', '3', '4','5','6','7','8','9','10','Jack','Queen','King']
    print()
    print("{0}: {1:0.1%} ".format(cards[i],busts/n))

if __name__ == '__main__': main()

main()