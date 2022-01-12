def main():
    print("This Program ilustrates a chaotic function")
    n = 10
    x = .25
    y = .26

    print("index {0:>10}{1:>10}".format(x, y))
    print("="*30)
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print("{2:<10}{0:^10.5f}{1:^10.5f}".format(x, y, (i+1)))
    print("="*30)

main()
