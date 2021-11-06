#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'gmail': 'mri99@gmail.com',
 'blog': 'myblog123',
 'luggage': '12345'}


import sys, pyperclip
#when no command line argument is provided
if len(sys.argv) < 2:
 print('Usage: python PassowrdLocker.py [account] - copy account password')
 sys.exit()
#first command line arg is the account name
account = sys.argv[1] 
#finding passwords in dictionary
if account in PASSWORDS:
 pyperclip.copy(PASSWORDS[account])
 print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account)
