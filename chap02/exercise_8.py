def main():
    print("Welcome! This program will convert Fahrenheit degrees into Celsius.")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is ", celsius, "degrees Fahrenheit.")

main()
    