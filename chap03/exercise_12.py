#Sum of the cubes of the first n natural numbers
def main():
    n = eval(input("What is the value of n? "))
    cube = sum(f ** 3 for f in range (n-1))
    print("The cube of the first", n, "natural numbers is", cube)

main()
