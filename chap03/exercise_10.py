import math

# Exercise 9
def tri(a,b,c):
    se = (a+b+c)/2
    area = math.sqrt(se*(se-a)*(se-b)*(se-c))
    print('The area of the triangle is: ', area)
    
tri(17,35,20)

# Exercise 10


def main():
    height, angle = eval(input(
        "What is the height of the house in feet, and the angle of the ladder in degrees? "))
    length = height / (math.sin((math.pi / 180 * angle)))
    print("The ladder is", round(length, 2), "feet in length")


main()
