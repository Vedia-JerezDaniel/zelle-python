print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number: "))

for _ in range(10):
    x = 3.9 * x * (1 - x)
    print(x)
   

