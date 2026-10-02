#program to calculate the value of pi using Leibniz series, Machin-Like formula and Monte Carlo Estimation

#no of iterations = 1000

pi = 3.141592653589793
print("pi = {}".format(pi))

#------------------------------------------------

#Leibniz Series

#we will start with S=0 and S = S + (-1)^k/(2k+1)

S = 0

for k in range (0, 1000):
    S = S + (-1)**k/(2*k+1)

leibniz = 4 * S
error = abs(pi - leibniz)/pi * 100

print("(Leibniz Series) pi = {}".format(leibniz))
print("Error% = {}".format(error))

#------------------------------------------------

#Machine-Like formula

#pi = 16arctan(1/5) - 4arctan(1/239)
#arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

arctan5 = 0
arctan239 = 0

for k in range (0, 1000):
    arctan5 = arctan5 + (-1)**k*(1/5)**(2*k+1)/(2*k+1)
    arctan239 =  arctan239 + (-1)**k*(1/239)**(2*k+1)/(2*k+1)

machin = 16*arctan5 - 4*arctan239
error = abs(pi - machin)/pi * 100

print("(Machin-Like Formula) pi = {}".format(machin))
print("Error% = {}".format(error))

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


montecarlo = 4*inside/total
error = abs(pi-montecarlo)/pi*100

print("(Monte Carlo Estimation) pi = {}".format(montecarlo))
print("Error% = {}".format(error))