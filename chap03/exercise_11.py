#Sum of the first n natural numbers

def main():
    n = eval(input("What is the value of n? "))
    ad = sum(range(n-1))
    print("The sum of of the first", n, "natural numbers is", ad)

main()
