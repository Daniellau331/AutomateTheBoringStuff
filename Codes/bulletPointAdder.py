#! python3

# bulletPointAdder.py - Adds Wikipedia bullet point to the start

# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

# Join the lines
text =  '\n'.join(lines)


pyperclip.copy(text)
