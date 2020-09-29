import fileinput

lines = []
isFloat = False
for line in fileinput.input():
	if line.find(".") != -1:
		isFloat = True
	x = line.split("\n")
	lines.append(float(x[0]))

result = 0.0
for i in lines:
	result = result + i

if not isFloat:
	result = int(result)

print(result)