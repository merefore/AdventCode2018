import numpy as np
from sets import Set
with open("input.txt","r") as f:
	data = f.readlines()

for i in xrange(len(data)):
	chars = list(data[i])
	if chars[-1] == '\n':
		del chars[-1]
	for j in xrange(len(data)):
		chars_compare = list(data[j])
		count_notsame = 0
		for k in xrange(len(chars)):
			if chars_compare[k] != chars[k]:
				count_notsame += 1
		if count_notsame == 1:
			index1 = i
			index2 = j

code1 = list(data[index1])
code2 = list(data[index2])

answer = ''

for p in xrange(len(code1)):
	if code1[p] == code2[p]:
		answer += code1[p]

print answer

