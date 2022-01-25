def main():
    n = eval(input("How many numbers do you have? "))
    sum = 0.0
    for _ in range(n):
        x = eval(input("Enter a number >> "))
        sum += x
    print("\nThe average of the numbers is", sum / n)

main()
