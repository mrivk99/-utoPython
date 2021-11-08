# A program that could search the text in your clipboard for phone numbers and
# email addresses, you could simply press ctrl-A to select all the text, press
# ctrl-C to copy it to the clipboard, and then run your program. It could
# replace the text on the clipboard with just the phone numbers and email
# addresses it finds.

import pyperclip,re
# Get the text off the clipboard.
# Find all phone numbers and email addresses in the text.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #area code (optional)
    (\s|-|\.)?                 #separator
    (\d{3})                   #first 3 digits
    (\s|-|\.)                 #separator
    (\d{4})                   #last 4 digits
    (\s*(ex|x|ext.)\s*(\d{2,5}))? #The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits
)''',re.VERBOSE)

emailRegex= re.compile(r'''(
[a-zA-Z0-9.%_+-]+ #username
@
[a-zA-Z0-9.-]+    #domain
(\.[a-zA-Z]{2,4})   #dot-something
)''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Paste them onto the clipboard.
if len(matches) > 0:
 pyperclip.copy('\n'.join(matches))
 print('Copied to clipboard:')
 print('\n'.join(matches))
else:
 print('No phone numbers or email addresses found.')
 
