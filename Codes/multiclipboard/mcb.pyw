#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#	 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#	 py.exe mcb.pyw list - Loads all keyworeds to clipboard.

# note: .pyw means that python will not show a terminal when it runs this program. 

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste();
elif len(sys.argv) ==2:
	# List keywords and load content. 
	if sys.argv[1].lower() == 'list' and len(sys.argv)==3:
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close();