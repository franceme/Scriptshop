#!/usr/bin/env python3

import os
import sys

gitignore='.gitignore'

if __name__ == '__main__':
	if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
		print("Please specify a valid file")
	elif (not os.path.exists(gitignore)):
		print('Please create a valid .gitignore file')
	else:
		with open(gitignore, 'a+') as foil:
			foil.write('\n' + str(sys.argv[1]) + '\n')