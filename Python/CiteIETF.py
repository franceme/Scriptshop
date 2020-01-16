#!/usr/bin/env python3

import os,sys,requests

if len(sys.argv) != 2:
    print('Usage: ####.py {IETF Number}')
    sys.exit()

res = requests.get("https://sysnetgrp.no-ip.org/rfc/rfcbibtex.php?type=RFC&number="+sys.argv[1])

if res.status_code == 200:
    print("https://tools.ietf.org/pdf/"+str(sys.argv[1])+".pdf\n")
    print(res.text)
else:
    print(res.status_code)
