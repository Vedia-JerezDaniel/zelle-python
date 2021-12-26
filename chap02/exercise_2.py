def main():
    print("This program computes the average of three exam scores.")

    score = list(eval(input("Enter three scores separated by commas: ")))
    num = len(score)
    average = sum(score) / num    

    print("The average of the scores is:", average)

main()
