#! python3
# mapit.py - Launches a map in he browser using an address from the command line or cllipboard.
# if there is no command line arguments, then the program will know to use the  contents of
# the clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
	# Get address from command line arguments. sys.argv stores a list of program's filename and command line arguments. 
	# len(sys.argv)>1 means the user enters command line arguments
	# sys.argv[1:] chop off the first element of the array.
	# if you enter this into the command line
	# mapit 870 Valencia St, San Francisco, CA 94110
	# the sys.argv variable will contain this list value:
	# ['mapit.py', '870', 'Valencia','St,','San','Francisco','CA','94110']
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard if there is no command line arguments.
	address = pyperclip.paste()

# launch the browser with the Google map URL, call webbrowser.open()
webbrowser.open('https://www.google.com/maps/place/'+address)