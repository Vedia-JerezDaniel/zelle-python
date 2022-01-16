def sumN(n):
    return 1 + sum(range(n,1,-1))
def sumNCubes(n):
    return 1 + sum(f**3 for f in range(n,1,-1))
def main():
    n = eval(input("Enter a value: "))
    N = sumN(n)
    NCubes = sumNCubes(n)
    print("The sum of the first {0} natural numbers is {1}, and the sum of the\n"
    "sum of the first {0} cubes is {2}".format(n, N, NCubes))

main()
