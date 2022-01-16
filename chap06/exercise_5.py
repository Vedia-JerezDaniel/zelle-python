import math

def pizzArea(diameter):
    return math.pi * ((.5 * diameter) ** 2)
def pizzPrice(cost, area):
    return cost / area

def main():
    price, d = eval(input("Enter the cost of the Pizza, and how big it was (comma separated): "))
    A = pizzArea(d)
    price_sqin = pizzPrice(price, A)
    print("The pizza has an area of {0} square inches".format(round(A, 2)))
    print("The price per square inch is about ${0}.".format(round(price_sqin, 2)))

main()

