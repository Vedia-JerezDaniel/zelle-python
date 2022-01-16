def nextGuess(guess, x):
    return (guess + x / guess) / 2

def main():
    x = eval(input("Find the square root of: "))
    y = eval(input("How many iterations of Newton's formula would you like?: "))
    g = x / 2
    
    for _ in range (y):
        g = nextGuess(g, x)
        print(g)
main()
