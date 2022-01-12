def main():
    print("This program calculates the future value\n", "of a 10-year investment.")

    principal = 900
    apr = 5

    print("{0:<} {1:>10}".format("Year", "Value"))
    print("+"*18)

    for i in range (10):
        principal *= 1 + .01 * apr
        print("{0:<8} ${1:<}.{2:0<3}".format(i+1, int(principal), int(principal%1 * 100)))

main()
