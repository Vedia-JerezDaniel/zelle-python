#This program finds every prime number less than or equal to input n
import math
def prime(n):
        #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
        x = math.sqrt(n)
        i = 2
        while i <= x:
                value = n % i
                            #if any value is divisble, break and close program
                if value == 0:
                        return
                else:
                        i += 1
        if n > 1:
            print(n)

def main():
    x = 0
    while True:
        x = eval(input("Input a positive whole number: "))
        if (x % 1 != 0):
            x = print("The number you entered was not whole!")
        elif (x < 1):
            x = print("The number you entered was not positive!")
        else:
            break
    for n in range(x):
        prime(n+1)

main()
