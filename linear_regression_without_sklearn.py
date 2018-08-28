import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

url = r'graph.csv'

coln=['X', 'Y']
graph = pd.read_csv(url, names = coln)
xx = graph.X.tolist() # adding value of x column to xx list
yy = graph.Y.tolist() # adding value of y column to yy list

plt.plot(xx, yy, 'ro')

#median data
x_mean = np.mean(xx)
y_mean = np.mean(yy)
plt.plot(x_mean, y_mean, 'g^')

#calculating calue of m and C as y = mx + c :
# for m = sum((x-x_mean)*(y-y_mean))/sum((x-x_mean)*(x-x_mean))
s_nume = 0
s_deno = 0
length = len(xx)

for i in range(length):
    s_nume = s_nume + ((xx[i]- x_mean)* (yy[i] - y_mean))
    s_deno = s_deno + ((xx[i]- x_mean)**2)
m_val = s_nume / s_deno # m = Snumerator/Sdenominator
c_val =y_mean - m_val * x_mean  # from eqn y = mx + c
# x and y regression values
x_reg = []
y_reg = []
for j in range(length):
    x_reg.append(j) #indendent value
    y_reg.append(x_reg[j] * m_val + c_val) #dependent value
plt.plot(x_reg, y_reg, 'r*')
plt.plot(x_reg, y_reg)

sum_num = 0    # sum of numerator for R^2
sum_den = 0    # sum of denominator for R^2
for k in range(length):
    sum_num = sum_num + ((y_reg[k] - y_mean)**2)
    sum_den = sum_den + ((yy[k] - y_mean)**2)
rsqr = sum_num / sum_den
plt.xlabel('Value of R ^ 2 ~')
plt.text(1, 5.5, rsqr) # displaying valur of R square
print(rsqr)
plt.show()
