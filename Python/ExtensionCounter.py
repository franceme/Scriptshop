#!/usr/bin/python3
import os
import sys
import json

extz={}
exten = ('.cpp','.aspx','.cs','.html','.asax','.h','.ino','.master','.java')
walk_dir = sys.argv[1]

for root, directories, filenames in os.walk(walk_dir):
	for filename in filenames:
		filepath=os.path.join(root,filename)
		ext=os.path.splitext(filename)[-1].lower()
		if ext in exten:
			if ext not in extz:
				extz[ext]={}
				extz[ext]['FileCount']=1
				extz[ext]['TotalLineCount']=1
				extz[ext]['TotalCharacterCount']=1
			else:
				extz[ext]['FileCount']+=1
			with open(filepath, 'r') as f:
				try:
					lengther=len(f.read())
				except:
					lengther=0
				extz[ext]['TotalLineCount']+=1
				extz[ext]['TotalCharacterCount']+=lengther



for key in extz:
	extz[key]['AverageCharacterCountPerLine']=round(extz[key]['TotalCharacterCount']/extz[key]['TotalLineCount'],3)

print(extz)