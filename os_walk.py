import os

path = 'C:\\Users\\arya\\Desktop\\CV\\'

print(os.listdir(path))

for (root, dirs, files) in os.walk(path, topdown = True):
	print(root)
	print(dirs)
	print(files)
	print('------------------------------->')
	
	