import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# center of squircle
a,b = -0,1.5
# little radius of squircle
r = 3
x = np.linspace(-r+a,r+a,100)
x_value = list(x) + list(reversed(list(x)))

def squircle(n):
    # x**n + y**n = r**n
    s1 = [(abs(v-a)**n) for v in x]
    s2 = [abs((r**n - abs(v))**(1/n)+b) for v in s1]
    s3 = s2 + [2*b-v for v in s2]        
    plt.plot(x_value, s3)
    plt.axis('equal')
    #plt.show()

for p in np.arange(0.25,3.6,0.25):
    squircle(p)
plt.show()