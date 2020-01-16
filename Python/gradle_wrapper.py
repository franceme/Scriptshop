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
	cmd = 'gradle --stop; ' + str(rawcmd) + ';gradle --stop'
	print(cmd);os.system(cmd)
