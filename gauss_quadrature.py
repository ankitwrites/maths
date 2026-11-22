integration = 0
c = [0.2369269, 0.4786287, 0.56888889, 0.4786287, 0.2369269]
d = [-0.9061798, -0.5384693, 0, 0.5384693, 0.9061798]
a = float(input("Enter Lower Limit: "))
b = float(input("Enter Upper Limit: "))

def f(x):
	return x
	
intloop = [0]*5

for i in range(5):
	intloop[i] = c[i]*((b-a)/2*f((b-a)/2*d[i]+(a+b)/2))

for i in range(5):
	integration = integration + intloop[i]

print("Integration of the function within the given limits is: ", integration)
