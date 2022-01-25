#This program determines if a value is prime.
import math
import sys
#Validate n as a positive whole number
def main():
    n = 0;
    while True:
        n = eval(input("Input a positive whole number: "))
        if (n % 1 != 0):
            n = print("The number you entered was not whole!")
        elif (n < 1):
            n = print("The number you entered was not positive!")
        else:
            break

    #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
    x = math.sqrt(n)
    i = 2
    value = n % i
    while i <= x:
        #if any value is divisble, break and close program
        if value == 0:
            print("The number is not prime.")
            sys.exit()
        else:
            i += 1
    print("The number is prime.")

main()
