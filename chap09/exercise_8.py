#write a program that simulates multiple games of blackjack
    #estimates the probability that the dealer will bust
    #ace is 1 or 11
    #must hit if less than 17
        #if ace == 11 makes more than 17 less than 21
            #otherwise ace is 1

    #bool variable hasAce to determine if hand has an ace

    #randrange(1, 13)
    #if x == 11 or x == 12 or x == 13
    #    x = 10

from random import randrange

def main():
    printIntro()
    n = eval(input("How many hands should I simulate? >> "))
    busts = simNHands(n)
    printSummary(busts, n)

def printIntro():
    print("This program is designed to simulate (n) games of blackjack")
    print('and will return the probability of the dealer "busting" or')
    print("going beyond 21.")
    print()

def simNHands(n):
    return sum(not simOneHand() for _ in range(n))

def simOneHand():
    x = simOneCard()
    y = simOneCard()
    hand = x + y
    while hand < 17:
        if hasAce(x) is True:
            if hand <= 10:
                x = 11
                hand += 10
            else:   x = 1
        if hasAce(y) is True:
            if hand <= 10:
                y = 11
                hand += 10
            else:   y = 1
        z = simOneCard()
        hand = hand + z
    return hand <= 21

def simOneCard():
    x = randrange(1, 13)
    if x in [11, 12, 13]:
        x = 10
    return x

def hasAce(x):
    return x == 1

def printSummary(busts, n):
    print()
    print("The dealer has a {0:0.1%} chance of busting.".format(busts/n))

if __name__ == '__main__': main()

main()