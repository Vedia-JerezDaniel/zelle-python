print("This Program ilustrates a chaotic function\n",
      'Number must be between 0 and 1')

x = eval(input("Enter Number: "))
for _ in range(10):
    x = 2.0 * x * (1-x)
    print(x)

print('The values stabilize around 0.5')

## EXERCISE 4

print("This Program ilustrates a chaotic function\n",
      'Number must be between 0 and 1')

x = eval(input("Enter Number: "))
for _ in range(20):
    x = 2.0 * x * (1-x)
    print(x)

print('The values stabilize around 0.5')


