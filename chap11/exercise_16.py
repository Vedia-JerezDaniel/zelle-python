from math import sqrt

class StatSet:
    def __init__(self):
        self.stats = []

    def addNumber(self, x):
        self.stats.append(x)

    def mean(self):
        sum = 0.0
        for num in self.stats: 
            sum += num
        return sum / self.count()

    def median(self):
        self.stats.sort()
        size = len(self.stats)
        midPos = size // 2
        return (
            (self.stats[midPos] + self.stats[midPos - 1]) / 2
            if size % 2 == 0
            else self.stats[midPos]
        )

    def stdDev(self):
        xbar = self.mean()
        sumDevSq = 0.0
        for num in self.stats:
            dev = xbar - num
            sumDevSq += dev * dev
        return sqrt(sumDevSq/(len(self.stats) - 1))

    def count(self):
        return len(self.stats)

    def min(self):
        self.stats.sort()
        return self.stats[0]

    def max(self):
        self.stats.sort(reverse=True)
        return self.stats[0]

def main():
    data = StatSet()
    for i in range(45):
        data.addNumber(i * 3/2)
    print('This is the length of data points: {}'.format(data.count()))
    print('This is the mean of data : {}'.format(data.mean()))
    print('This is the median of data : {}'.format(data.median()))
    print('This is the Standard deviation of data : {:1f}'.format(data.stdDev()))
    print('This is the minimum point of data points: {}'.format(data.min()))
    print('This is the max point of data points: {}'.format(data.max()))
    
main()
    