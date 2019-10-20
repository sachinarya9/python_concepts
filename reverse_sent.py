reverse_string = ''

text_string = input('Enter the text string')

words = text_string.split(' ')

for each_word in words:
	
	reverse_word = ''
	for ind in range(len(each_word)-1, -1, -1):
		
		reverse_word += each_word[ind]
	
	reverse_string = reverse_string + ' ' + reverse_word
	
print(reverse_string)

