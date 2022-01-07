import math

def vs():
    radius = eval(input("Please enter the radius: "))
    volume = 4/(3*math.pi*radius**3)
    area = 4*math.pi*radius**2
    print("The volume is: ", volume)
    print("The area is: ", area)

vs()


def main():
    price, d = eval(input("Please enter the cost of the Pizza, and size (price , size): "))
    A = math.pi*((.5 * d)**2)
    price_sqin = price / A
    print("The price per square inch is", round(price_sqin, 2))

main()
