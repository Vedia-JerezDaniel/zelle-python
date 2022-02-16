import sys
sys.setrecursionlimit(1000)

def factorial(n):
    fact = 1
    for factor in range(n,1,-1):
        fact *= factor
    return fact

def iterative_options(n, k):
    x = factorial(n)
    y = factorial(k) * factorial(n - k)
    return x / y

def recursive_options(n, k):
    if k == 1:
        return n
    elif n < k:
        return 0
    else:
        return recursive_options(n - 1, k - 1) + recursive_options(n-1, k)


print(iterative_options(72, 5))
print(recursive_options(72, 5))
    