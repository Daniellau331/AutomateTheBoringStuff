#! python3
# example of deleting files throught a python program
# It is better to print the filename before the deletion. 

import os

for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink(filename)
		print(filename)