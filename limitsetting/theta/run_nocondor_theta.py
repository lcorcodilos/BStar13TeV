# !/bin/python
import subprocess
import glob
import copy
import re
import sys
import os
from optparse import OptionParser


parser = OptionParser()

parser.add_option('--file', metavar='F', type='string', action='store',
                  dest='file',
                  default='analysis_bsTEMPLATE.py',
                  help='analysis file')


parser.add_option('--uidir', metavar='F', type='string', action='store',
                  dest='uidir',
                  default=None,
                  help='crab UI directory')


(options, args) = parser.parse_args()

argv = []

outfile = options.file.split('.')[0] 


uidir = outfile

commands1 = []
commands2 = []
commands3 = []


commands1= [
    'rm analysis.py',
    'rm -rf analysis/',
    'rm -rf '+options.uidir,
    'rm analysis.tgz',
    'cp ' + options.file + ' ./analysis.py',
    './utils2/theta-auto.py',
    'mkdir ' + options.uidir,
    'cp -r analysis ' + options.uidir
] 


for s in commands1 :
    print 'executing ' + s
    subprocess.call( [s], shell=True )


