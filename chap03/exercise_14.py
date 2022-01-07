def main():
    n = eval(input("How many numbers would you like to average? "))
    x = eval(input(": "))
    for f in range (n+1):
        # y = eval(input(": "))
        x = float(x) + float(f)
    print("Your final average is: ", x / n)

main()

import math


def pi():
    k = 1
    s = 0
    n = eval(input("How many numbers would take? "))
    for f in range(1, n):
        # even index elements are positive
        if f % 2 == 0:  s += 4 / k
        else:  s = abs(s - (4 / k))
        # denominator is odd
        k += 2
    print("Your pi estimation is: ", s)
    print("Your error is: ", (math.pi - s))

pi()


