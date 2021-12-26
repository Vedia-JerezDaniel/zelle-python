def main():
    print("Welcome! This program will kindly convert", "\n", "degrees Celsius into Fahrenheit.")
    tem=[]
    res=[]
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature for measure " + str(i)+ ": "))
        tem.append(celsius)
        fahrenheit = (celsius * 9/5) +32
        res.append(fahrenheit)
    print("The temperatures are ", res, "degrees Fahrenheit.")

main()
