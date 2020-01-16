#!/usr/bin/python3
import os
import sys
import json

extz={}
walk_dir = sys.argv[1]

for root, directories, filenames in os.walk(walk_dir):
	for filename in filenames:
		filepath=os.path.join(root,filename)
		ext=os.path.splitext(filename)[-1].lower()
		if ext not in extz:
			extz[ext]={}
			extz[ext]['FileCount']=1
		else:
			extz[ext]['FileCount']+=1

print(extz)
