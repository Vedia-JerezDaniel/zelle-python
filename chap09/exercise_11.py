from random import randrange

def main():
    printIntro()
    n = eval(input("Simulations: "))
    return simNRolls(n)

def printIntro():
    print("This program is intended to simulate the rolling of five six-sided")
    print("dice to approximate the probability of rolling five-of-a-kind.")

def simNRolls(n):
    totFive = 0
    for _ in range (n):
        if not fiveOfAKind():
            totFive = totFive
        else:
            totFive += 1
    return totFive

def fiveOfAKind():
    a, b, c, d, e, f = simOneRoll()
    return a == b == c == d == e == f

def simOneRoll():
    dice = []
    for _ in range (6):
        x = randrange(1, 6)
        dice.append(x)
        
    print(dice)
    return dice

if __name__ == '__main__': main()

main()