import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
x_value = list(x) + list(reversed(list(x)))

def squircle(n):
    # x**n + y**n = 1
    s1 = [(abs(v)**n) for v in x]
    s2 = [((1 - abs(v))**(1/n)) for v in s1]
    s3 = s2 + [-v for v in s2]        
    plt.plot(x_value, s3)
    plt.axis('equal')
    #plt.show()

for p in np.arange(0.25,3.6,0.25):
    squircle(p)
plt.show()