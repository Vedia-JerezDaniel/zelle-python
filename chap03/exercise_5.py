def main():
    lbs = eval(input("How many pounds of coffee is in the order?     "))
    cost = (10.50 + .86) * lbs + 1.50
    # 1.5 is overhead cost
    print("Your order will cost a total of $", round(cost, 2))

main()
