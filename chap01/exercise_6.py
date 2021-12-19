import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

print("This Program ilustrates a chaotic function")
n = 100

x = eval(input("Enter a value between 0 and 1: "))

la = list()
lb = list()
lc = list()

def a(n, x):
    for _ in range(n):
        x = 3.9 * x * (1-x)
        la.append(x)
        print(la)

a(n, x)

def b(n, x):
    for _ in range(n):
        x = 3.9 * (x-x*x)
        lb.append(x)

b(n, x)

def c(n, x):
    for _ in range(n):
        x = 3.9 *x-3.9*x*x
        lc.append(x)

c(n, x)

df = pd.DataFrame(list(zip(la, lb, lc)), columns =['mod_A', 'mod_B', 'mod_C'])

df.sample(10)

fig = plt.figure()
ax = plt.axes()

x1 = np.linspace(0, 100, 100)
plt.plot(x1, df.mod_A)
plt.plot(x1, df.mod_B)
plt.plot(x1, df.mod_C);
plt.show()


