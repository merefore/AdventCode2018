import numpy as np
with open("input.txt","r") as f:
	data = f.readlines()
data = [float(i) for i in data]
print np.sum(data)