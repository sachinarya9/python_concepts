input_string = 'Hello world'
previous_char = ''
space_found = 0
string_req = ''
for char in input_string:
	if char == ' ':
		string_req = previous_char + ' '
		space_found = 1
		continue
	elif space_found:
		string_req += char
		
	previous_char = char
	
print(string_req)