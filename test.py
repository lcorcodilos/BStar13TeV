#! /usr/bin/env python
import glob
import math
import sys
import re



files = sorted(glob.glob("*job*of*.root"))


j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?).root', f).group(1),""))

files_to_sum = list(set(j))

for f in files_to_sum:
	print 'hadd ' + f + " " + f.replace('.root','_job*.root') 


