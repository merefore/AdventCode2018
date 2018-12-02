import numpy as np
from sets import Set
with open("input.txt","r") as f:
	data = f.readlines()

num_two = 0
num_three = 0

for item in data:
	chars = list(item)
	x,counts = np.unique(chars, return_counts=True)
	three = 0
	two = 0
	for i in xrange(0,len(counts)):
		if counts[i]==2:
			two += 1
		if counts[i]==3:
			three += 1
	if two>0:
		num_two += 1
	if three>0:
		num_three += 1

print num_two
print num_three
print num_two*num_three