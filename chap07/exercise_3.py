def main():
    x = eval(input("What is the number grade? "))
    # x = 84
    if x >= 90:
        print('A')
    elif 90 > x >= 80:
        print('B')
    elif 80 > x >= 70:
        print('C')
    elif 70 > x >= 60:
        print('D')
    else:
        print('F')
main()
