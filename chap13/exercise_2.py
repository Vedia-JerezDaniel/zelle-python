class FibCounter:
    def __init__(self):
        self.fibcount = 0

    def getCount(self):
        return self.fibcount

    def fib(self, n):
        self.fibcount += 1
        return 1 if n < 3 else self.fib(n-2) + self.fib(n-1)
    
    def resetCount(self):
        self.fibcount = 0


count = FibCounter()
count.getCount()
count.fib(23)
count.getCount()
count.resetCount()
