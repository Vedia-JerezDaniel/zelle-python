#While loop to determine rule of 72

def main():
    apr = eval(input("What is the annualized interest rate? "))
    apr = .01*apr
    principal = eval(input("What is the initial principal? "))

    p = principal
    interest = 0
    years = 0

    while principal > .5 * p:
        years += 1
        interest = p * apr
        p += interest

    print('Final amount plus interests: {:.1f}'.format(p))
    print('Number of years to double investment: {:d}'.format(years))

main()