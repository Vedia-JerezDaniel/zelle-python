def grade(score):
    grades = ["F" for _ in range(60)]
    for _ in range(60, 70):
        grades.append("D")
    for _ in range(70, 80):
        grades.append("C")
    for _ in range(80, 90):
        grades.append("B")
    for _ in range(90, 100):
        grades.append("A")
    return grades[score]

def main():
    n = (eval(input("Enter a number grade: ")))
    x = grade(n)
    print(x)
    
main()
