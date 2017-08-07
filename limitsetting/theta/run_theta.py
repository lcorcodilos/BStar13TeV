# !/bin/python
import subprocess
import glob
import copy
import re
import sys

from optparse import OptionParser


parser = OptionParser()

parser.add_option('--file', metavar='F', type='string', action='store',
                  dest='file',
                  help='analysis file')
parser.add_option('--dir', metavar='F', type='string', action='store',
                  dest='dir',
                  default=None,
                  help='directory')
parser.add_option('--hand', metavar='F', type='string', action='store',
                  dest='hand',
                  default=None,
                  help='handedness')

(options, args) = parser.parse_args()

argv = []

outfile = options.file.split('.')[0] 



commands = [
    'rm -rf ' + options.dir,
    'mkdir ' + options.dir,
    'cd ' + options.dir,
    'cp ../' + options.file + ' ./analysis.py',
    'cp ../BStarCombinationHistos_'+options.hand+'_Allhadronic.root ./'
    '../utils2/theta-auto.py',
    'mkdir results',
    'mv *limit*.txt results/',
    'cp analysis.py results/',
    'cp *.root results/',
    'tar -cz results/ > results_' + outfile + '.tgz'
    ]

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )

