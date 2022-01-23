def main():
    
    x = eval(input("Insert KM speed: "))
    y = 90 + 7
    t = x - y
    if t >= 0:
        fine = (t // 5) * 5 + 50
        if x >= 140:
            fine = fine + 200
        print("You owe ${0}.".format(fine))
        print("If you pay in the next 7 days, penalty is ${0}.".format(fine/2))
    else:
        print("NO speed violation.")

main()
