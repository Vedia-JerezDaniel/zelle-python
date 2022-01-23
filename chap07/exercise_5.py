def BMI(weight, height):
    return (weight / height / height) *10000

def main():
    x, y = eval(input("What is your weight (in Kgs) and height (in cm)?: "))
    bmi = BMI(x, y)
    print('Your BMI is {:2.2f}:'.format(bmi))
    
    if 19 <= bmi <= 25:
        print("You are within the arbitrary healthy range.")
    elif bmi < 19:
        print("You are below the arbitrary healthy range.")
    else:
        print("You are above the arbitrary healthy range.")
main()
