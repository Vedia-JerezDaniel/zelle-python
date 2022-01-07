def main(i):
    print("Calculator program")
    x = eval(input())
    y = eval(input())
    if i == 'added':
        print("summ", str(x+y))
    if i == 'rest':
        print("substraction", str(x-y))
    if i == 'mult':
        print("multiplication", str(x*y))
    if i == 'divi':
        print("division", str(x/y))


main('added')
