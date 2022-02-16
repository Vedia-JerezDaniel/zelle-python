def fib(n):
    print("Computing fib({})".format(n))
    if n < 3:    return 1
    print("Leaving fib({0}), returning {1}".format(n, fib(n-2) + fib(n-1)))
    return fib(n-2) + fib(n-1)
        


fib(4)
