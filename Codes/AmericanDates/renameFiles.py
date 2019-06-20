#! python3
# renameFiles.py 
# usage: renaming files with American-style (MM-DD-YYYY) dates to european-style (DD-MM-YYYY) dates


import shutil, os, re

# create a regex that matched files with the American datae format.

datePattern = re.compile(r"""^(.*?)  # text before the date
	((0|1)?\d)-						# one or two digits for the month
	((0|1|2|3)?\d)-					# one or two digits for the day
	((19|20)?\d\d)					# four digits for the year
	(.*?)$							# text after the date
	""",re.VERBOSE)

# passing re.VERBOSE for the second argument will allow comments and whitespace in the regex string. (more readable)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename) 

	# Skop files without a date.
	if mo == None:
		continue

    # Get the different parts of the filename.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the European-styly filename.
	euroFilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart

	# Get the full, absolute file paths.
	asbWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(asbWorkingDir,amerFilename)
	euroFilename = os.path.join(asbWorkingDir,euroFilename)

	# Rename the files.
	print('before ---> "%s"'%(beforePart))
	print('monthPart ---> "%s"'%(monthPart))
	print('dayPart ---> "%s"'%(dayPart))
	print('yearPart ---> "%s"'%(yearPart))
	print('afterPart ---> "%s"'%(afterPart))

	print('Renaming "%s" to "%s"...'%(amerFilename,euroFilename))
	shutil.move(amerFilename,euroFilename)  #uncomment after testing