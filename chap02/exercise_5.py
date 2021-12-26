def main(year):
    print("This program calculates the future value of a", year, "-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in perecents: "))
    for _ in range(year):
        principal = principal * (1 + (apr * .01))
    print("The value in", year, "years is", principal)

main(10)


def cumm(year):
    print("This program calculates the future value and cumulative sum of a", year,"-year investment.")
    inv_year = eval(input("Yearly investment: "))
    apr = eval(input("Enter the annual interest rate in percentage: "))
    for _ in range(year):
        principal = (inv_year * year) * (1 + (apr * .01))
    print("The value in", year, "years is", principal)

cumm(10)


def comp(year):
    print("This program calculates the compounded investment", year,"-year investment.")
    inv_year = eval(input("Yearly investment: "))
    apr = eval(input("Enter the annual interest rate in percentage: "))
    per = eval(input("Enter the period of time: "))
    for _ in range(year):
        inv_year = inv_year * year* (1 + (apr * .01))
        second = per*inv_year*(1 + (apr * .01)/(per*year))
    print("The value in", year, "years is", inv_year)
    print("The value of second in", year, "years is", second)

comp(10)
