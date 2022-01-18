def fibonnaci(n):
    x,y,z = 0, 1, 0

    for _ in range (n+1):
        z = x + y
        x = y
        y = z
        print(z)
    return y

def main():
    n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
    y = fibonnaci(n)
    print("The {0} Fibonnaci number is {1}.".format(n, y))

main()
