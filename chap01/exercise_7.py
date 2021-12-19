import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


print("This Program ilustrates a chaotic function")
n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a value between 0 and 1: "))
y = eval(input("Enter a different value between 0 and 1: "))

la = list()
lb = list()

for _ in range(n):
    z = 2.9 * x * (1-x)
    la.append(z)

for _ in range(n):
    z = 2.9 * y * (1-y)
    lb.append(z)
    

df = pd.DataFrame(list(zip(la, lb)), columns =['mod_A', 'mod_B'])
print(df.head(8))

# x1 = np.linspace(0, 1, n)
# plt.plot(x1, df.mod_A)
# plt.plot(x1, df.mod_B);
# plt.show()
