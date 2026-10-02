#program to calculate the value of pi using Leibniz series, Machin-Like formula and Monte Carlo Estimation

#------------------------------------------------

#Leibniz Series

#we will start with S=0 and S = S + (-1)^k/(2k+1)

S = 0

for k in range (0, 1000):
    S = S + (-1)**k/(2*k+1)

print("(Leibiz Series) pi = {}".format(4*S))

#------------------------------------------------

#Machine-Like formula

#pi = 16arctan(1/5) - 4arctan(1/239)
#arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

arctan5 = 0
arctan239 = 0

for k in range (0, 1000):
    arctan5 = arctan5 + (-1)**k*(1/5)**(2*k+1)/(2*k+1)
    arctan239 =  arctan239 + (-1)**k*(1/239)**(2*k+1)/(2*k+1)

print("(Machin-Like Formula) pi = {}".format(16*arctan5 - 4*arctan239))

#------------------------------------------------

#Monte Carlo Estimation

import random

#A square of area = 1 and a qaurter circle of area = pi/4 inside the square
#pi = 4 * points inside quarter-circle/total points inside the square

total = 1000
inside = 0

for i in range(0, total):
    x = random.random()
    y = random.random()
    if (x**2 + y ** 2 <= 1):
        inside = inside + 1

print("(Monte Carlo Estimation) pi = {}".format(4*inside/total))