from sys import path

path.append('..\\modules')
print(path)

import module

zeroes = [0 for _ in range(5)]
ones = [1 for _ in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

