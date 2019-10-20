input_string = '{a b { a b } { c { b d } e} b a}'
bracket = 0
incomplete_string_list = []
complete_string_list = []
complete_string = 0
string9 = ''
for each_char in input_string:
	if '{' in each_char:
		if bracket == 1:
			incomplete_string_list.append(string9)
			string9 = ''
			continue
		
		bracket = 1
		continue
	
	elif '}' in each_char.strip():
		
		if complete_string == 1:
			complete_string_list.append(incomplete_string_list[len(incomplete_string_list)-1])
			incomplete_string_list.pop(len(incomplete_string_list)-1)
			complete_string = 0
			continue
		
		
		complete_string_list.append(string9)
		string9 = ''
		
		bracket = 0
	
	else:	
		if bracket == 0 and each_char.strip() != '':
			complete_string = 1
			if each_char in incomplete_string_list[len(incomplete_string_list)-1]:
				incomplete_string_list[len(incomplete_string_list)-1] = incomplete_string_list[len(incomplete_string_list)-1] + each_char + '*'
			
			else:
				
				incomplete_string_list[len(incomplete_string_list)-1] = incomplete_string_list[len(incomplete_string_list)-1] + each_char
				
		if each_char in string9:
			string9 = string9 + each_char.strip() + '*'
		else:
			string9 += each_char.strip()
		
print(complete_string_list)