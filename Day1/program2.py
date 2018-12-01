import numpy as np
from sets import Set
with open("input.txt","r") as f:
	data = f.readlines()
data = [float(i) for i in data]

init = 0

freqs = Set()
i = 0
x = True
while x == True:
	init = init + data[i%len(data)]
	if init in freqs:
		x = False
		print init
	freqs.add(init)
	i += 1
	if i == 1000000:
		x = False
	if i%996 == 0:
		print i/len(data)
