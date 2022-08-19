# Order of Operations
xrange = range(11, 33)


for x in xrange:
	x_variable = x
	y_variable = ((3 * x_variable**2) + (6 * x_variable)) / (2 * x_variable)
	print(f"{x_variable}")
	print(f"\t{y_variable}")