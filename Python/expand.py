#!/usr/bin/env python3

##Imports
import os
import sys
import subprocess
from copy import deepcopy as dc

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
	base = dc(rawcmd)
	if (sys.argv[1].startswith(':')):
		alias = sys.argv[1][1:]
		with open(str(os.environ['HOME']) + '/.bash_aliases','r') as aliases:
			for line in [split.strip() for split in aliases.readlines() if not split.strip().startswith('#')]:
				if line.startswith('alias ' + str(alias)):
					rawcmd = toStr(sys.argv[2:], line[line.index("'")+1:len(line)-1])
		if base == rawcmd:
			with open(str(os.environ['HOME']) + '/utilities.aliases','r') as aliases:
				for line in [split.strip() for split in aliases.readlines() if not split.strip().startswith('#')]:
					if line.startswith('alias ' + str(alias)):
						rawcmd = toStr(sys.argv[2:], line[line.index("'")+1:len(line)-1])
	os.system(rawcmd)
