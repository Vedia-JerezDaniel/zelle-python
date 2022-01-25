#Goldbach conjecture
#Every even number is the sum of two prime numbers
#This program gets a number from the user, validates it being even,
#then finds two primes that add up to that number

import math

def primeNum(n):
        x = math.sqrt(n)
        i = 2
        while i <= x:
                value = n % i
                if value == 0:
                    return None
                else:
                    i += 1
        return n

def main():
    x = eval(input("Input a positive whole number: "))
    while True:
        if x == 0:
            x = eval(input("Your number must be higher than 0: "))
        elif (x < 1):
            x = eval(input("The number you entered was not positive: "))
        elif (x % 2 != 0):
            x = eval(input("The number you entered was not even: "))
        else:
            n = x
            break
        
    while n > 0:
            prime = primeNum(n)
            if prime != None:
                prime2 = x - prime
                test = primeNum(prime2)
                if test != None:
                    print("{0} + {1} = {2}".format(prime, prime2, x))
            n = n - 1

main()
