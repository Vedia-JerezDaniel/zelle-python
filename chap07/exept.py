import math
from tkinter.tix import MAX

def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError:
        print ("\nNo real roots")

main()

import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2 )
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots")
        else:
            print("You didn’t give me the right number of coefficients.")
    except NameError:
        print("\nYou didn’t enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")
main()

# ---- MAX
"""No es eficiente
    """

def main():
    n = eval(input("How many numbers are there? "))
# Set max to be the first value
    max = eval(input("Enter a number >> "))
    # Now compare the n-1 successive values
    for _ in range(n-1):
        x = eval(input("Enter a number >> "))
    if x > max:
        max = x
    print("The largest value is", max)
    
main()


