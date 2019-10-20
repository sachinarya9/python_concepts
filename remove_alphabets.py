input_string = 'acfhijgdecuwxz'
char_ind = 0
# for ind,char in enumerate(input_string):
while char_ind < len(input_string):
	char = input_string[char_ind]
	# first asc value
	removed_char = 0
	asc_value = ord(char)
	i = char_ind + 1
	while i < len(input_string):
		second_asc_value = ord(input_string[i])
		# if i == 5:
			# print('jim',input_string[i])
		# print(input_string[i],second_asc_value)
		if second_asc_value == asc_value + 1:
			asc_value = second_asc_value
			print('yeah',input_string[i],second_asc_value)
			removed_char = 1
			if char_ind == 0:
				input_string = input_string[i+1:]
			else:
				# print(i, input_string[i+1:])
				input_string = input_string[0:char_ind] + input_string[i+1:]
				i -= 2
		else:
			
			break
		
		i += 1
		print('i is',i)
	if removed_char == 1:
		
		char_ind -= 1
		
	else:
	
		char_ind += 1
	
	
print(input_string)