def countingValleys(n, s):
	down = 0
	up = 0
	valley_visited = 0
	for ind,each_elem in enumerate(s):
		if each_elem == 'D':
			# print('d',each_elem)
			down = down + 1
			if up != 0:
				down -= down
				up = up - 1
		else:
			# print('u',each_elem)
			up += 1
			if down != 0:
				down -= 1
				up -= 1
		print(down,up)
		if down == 1 and up == 0:
			valley_visited +=1
	return valley_visited
	
res = countingValleys(8,['U','D','D','D','U','D','U','U'])
print(res)