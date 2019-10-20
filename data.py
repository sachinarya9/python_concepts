data = {'text2':'Tyrion','text9':'Jaime','text7':'Tyrion'}
final_data = {}
for k, v in data.items():
	if v not in final_data.keys():
		final_data[v] = []
		final_data[v].append(k)
	else:
		final_data[v].append(k)
print(final_data)

		