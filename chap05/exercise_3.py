def main():
    for _ in range (10):
        #receive grade from teacher in number format
        n = (eval(input("Enter a number grade: ")))

        #Use the append method to assign variables to values
        grade = ["F" for _ in range(60)]
        for _ in range(60, 70):
            grade.append("D")
        for _ in range(70, 80):
            grade.append("C")
        for _ in range(80, 90):
            grade.append("B")
        for _ in range(90, 300):
            grade.append("A")

        #print results 
        print(grade[n])

main()
