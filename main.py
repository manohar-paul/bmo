#functions in bmo
import math

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# x- coordinates of the Bflies
x_ordinate = []
for i in range(30):
    x_ordinate.append(-i/10)
    x_ordinate.append(i/10)

# y - coordinates of Bflies    
y_ordinate = []
for i in range(30):
    y_ordinate.append(-i/10)
    y_ordinate.append(i/10)

#print(len(x_ordinate))
#print(len(y_ordinate))

# UVi of each Bfly at t = 0
i, t = (60, 60)
uv = [[0]*t] * i

# UV reflected by ith Bfly to jth Bfly at t = 0
i, j = (60, 60)
uvdistribution = [[0]*j] * i

# 3 peak function of (x,y).
def f(x, y):
    
    p = 3 * (1 - x)**2
    p = p * (math.exp((-(x**2) - (y+1)**2)))
    q = (x/5) - x**3 - y**5
    q = q*(math.exp((-(x**2) - (y**2))))
    r = math.exp(-(x+1)**2 - y**2)
    s = p - 10*q -r/3
    return s

# distance between ith and jth Bfly
def distance(i, j):
    xdd = (x_ordinate[i] - x_ordinate[j])**2
    ydd = (y_ordinate[i] - y_ordinate[j])**2
    return (xdd + ydd)**0.5

# 1/distance of ith and jth Bfly
def inverse_d(i, j):
    if (i != j):
        return (distance(i,j))**(-1)
    elif (i == j):
        return 0

# sum of all inverse distances of Bflies from ith Bfly.
def reversed_sum(i):
    k = 0
    sum = 0
    while(k < 60):
        if(i != k):
            sum = sum + inverse_d(i,k)
        k = k + 1
    return sum


# algorithm trial 1 :-
t = 1
while(t < 50):
    i = 2
    while(i < 60):
        uv[i][t] = max(0, 0.5*uv[i][t-1] + 2*f(x_ordinate[i], y_ordinate[t]))
        j = 2
        while (j < 60):
            uvdistribution[i][j] = (uv[i][t] * inverse_d(i, j)) / reversed_sum(i)
            j = j + 1
        
        maxuvd = [max(i) for i in zip(*uvdistribution)][58]
        j = 2
        while (j < 60):
            if(uvdistribution[i][j] == maxuvd):
                lmatej = j
                break
            j = j + 1
        
        if (distance(i, lmatej) != 0):    
            x_ordinate[i] = x_ordinate[i] + (0.15*(x_ordinate[lmatej] - x_ordinate[i])) / distance(i, lmatej)
            y_ordinate[i] = y_ordinate[i] + (0.15*(y_ordinate[lmatej] - y_ordinate[i])) / distance(i, lmatej)  
        
        
        i = i + 1
        
    t = t + 1
    
for i in range(30):
    print(x_ordinate[i], end = ',')
    print(y_ordinate[i])


    
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
p = 2
while(p < 60):
    ax.scatter3D(x_ordinate[p], y_ordinate[p], 0, color = "green")
    plt.title("simple 3D scatter plot")
    p = p + 1
 
# show plot
plt.show()
