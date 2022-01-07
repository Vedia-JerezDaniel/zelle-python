def main():
    n = eval(input("How many numbers would you like to add? "))
    x = eval(input(": "))
    for f in range (n+1):
        # y = eval(input(": "))
        x = x + f
    print("Your final sum is: ", x)

main()
