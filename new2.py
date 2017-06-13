f = open("C:\\Users\\Helen\\python\\out.txt")
#line = f.readline()
#while line:
	#print (line)
	#print(line,end='')
	#line = f.readline()
for line in f:
	print (line,end='')
f.close()
print ("你好")