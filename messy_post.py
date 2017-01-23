#! /usr/bin/env python
#doopity
import re
import os
import subprocess
from os import listdir
from os.path import isfile, join
import glob
import math
import ROOT
from ROOT import *
import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
(options, args) = parser.parse_args()

cuts = options.cuts

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
lumi = Cons['lumi']
ttagsf = Cons['ttagsf']
wtagsf = Cons['wtagsf']
xsec_bsr = Cons['xsec_bsr']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
nev_bsr = Cons['nev_bsr']
nev_bsl = Cons['nev_bsl']
nev_ttbar = Cons['nev_ttbar']
nev_qcd = Cons['nev_qcd']
nev_st = Cons['nev_st']

commands = []

f = 'TWanalyzersignalright2000_Trigger_nominal_none_PSET_default.root'

coup = 'right'
mass = f.replace('TWanalyzersignal'+coup,'')[:4].replace("_","")
xsec_sig = xsec_bsr[mass]
if coup =='right':
	nev_sig = nev_bsr[mass]
if coup =='left':
	nev_sig = nev_bsl[mass]
	
commands.append('rm ' + f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup))	 
commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' -w ' + str(lumi*xsec_sig/nev_sig))
commands.append('mv '+f+' temprootfiles/')
commands.append('mv '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' rootfiles/')

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )