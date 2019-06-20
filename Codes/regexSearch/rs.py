#!  python3

# A program that opens all .txt files in a folder and searches for any line that matches a provided regular expression.
# It will print the results to the screen.

import glob , re



path = 'S:\\pythonscript\\regexSearch'

regex = 'am'


textRegex = re.compile(regex)

# opens all .txt files in a folder
for filename  in glob.glob(os.path.join(path,'*.txt')):
	file = open(filename)
	fileContent = file.read()
	result = textRegex.search(fileContent)
	print(result)