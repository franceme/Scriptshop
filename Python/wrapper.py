#!/usr/bin/env python3

##Imports
import os
import sys
import subprocess

def toStr(lyst, cmd=None):
	string = ''

	if cmd is not None:
		string = str(cmd) + ' '

	for item in lyst:
		string += str(item) + ' '
	return string

'''####################################
#The main runner of this file, intended to be ran from
'''####################################
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Please enter a valid argument.')
		sys.exit()
	
	rawcmd = toStr(sys.argv[1:])
	if (sys.argv[1].startswith(':')):
		alias = sys.argv[1][1:]
		with open(str(os.environ['HOME']) + '/.bash_aliases','r') as aliases:
			for line in [split.strip() for split in aliases.readlines() if not split.strip().startswith('#')]:
				if line.startswith('alias ' + str(alias)):
					arg = ['']
					if len(sys.argv) > 2:
						arg = sys.argv[2:]
					rawcmd = toStr(arg, line[line.index("'")+1:len(line)-1])

	cmd = 'nohup ' + str(rawcmd) + '>/dev/null 2>&1 &'
	print(cmd);os.system(cmd)
