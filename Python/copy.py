#!/usr/bin/python3
import os
import sys
import json
import shutil
import glob
import math

extz={}
walk_dir = sys.argv[1]
out_dir = sys.argv[2]

def verbose_copy(src, dst):
    try:
        print(src)
        sizeCheck = file_size(src)
        if not sizeCheck:
            print('Ignoring file: ' + str(src))
            return None
        else:
            print('copying\n {!r}\n to {!r}'.format(src, dst))
            return shutil.copy2(src, dst)
    except Exception as E:
        print('Failing at file: ' + str(src))
        print(E)
        return None

idx = ['bytes', 'KB', 'MB', 'GB', 'BROKEN']

def convert_bytes(num):
    for x in idx:
        if (x is 'BROKEN'):
            return (idx.index(x), 0)
        if num < 1024.0:
            num = math.ceil(num)
            return (idx.index(x), int(num)) #"%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        (x, size) = convert_bytes(file_info.st_size)
        print(str(size)+' '+str(idx[x]))
        if (x > 3):
            print('File is greater than GBs in size')
            return False
        elif (x == 3) and (size > 2):
            print('File is greater than 2 GBs in size')
            return False
        else:
            return True
    else:
        print('File is not a file')
        return True

shutil.copytree(
    walk_dir, out_dir,
    copy_function=verbose_copy
)