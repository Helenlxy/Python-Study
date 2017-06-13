principal = 1000
rate = 0.05
numyears = 5
year = 1
f = open ("C:\\temp\\out","w")
while year <= numyears:
	principal = principal * (1 + rate)
	print("%3d %0.2f" % (year,principal),file = f)
	print("%3d %0.2f" % (year,principal))
	year += 1