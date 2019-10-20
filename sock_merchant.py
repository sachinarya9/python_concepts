import cal_power_lambda_func

def sockMerchant(n, ar):
	sock_dict = {}
	total_socks = 0
	for each_element in ar:
		if each_element not in sock_dict.keys():
			sock_dict[each_element] = 1
		else:
			sock_dict[each_element] = sock_dict[each_element] + 1
	print(sock_dict.values())
	for values in sock_dict.values():
		print('v',values)
		total_socks = total_socks + int(values/2)
		print('t',total_socks)
	return total_socks
res = sockMerchant(9,[10,20,20,10,10,30,50,10,20])
print(res)