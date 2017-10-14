#! /usr/bin/env python
#NOT BUILT FOR MULTIPLE LUMIS
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
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
(options, args) = parser.parse_args()

cuts = options.cuts

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()

#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = str(int(cLumi))+'pb'

xsec_bsr = Cons['xsec_bsr']
xsec_bsl = Cons['xsec_bsl']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']


files = sorted(glob.glob("*job*of*.root"))

j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?)_PSET', f).group(1),""))

files_to_sum = list(set(j))

# Sum jobs
commands = []
commands.append('rm *.log') 
commands.append('rm -rf notneeded')
for f in files_to_sum:
	commands.append('rm '+f) 
	commands.append('hadd ' + f + " " + f.replace('_PSET','_job*_PSET') )
	commands.append('mv ' +  f.replace('_PSET','_job*_PSET') + ' temprootfiles/')


# QCDHT
commands.append('rm rootfiles/'+Lumi+'/TWminitree_QCD_PSET_'+cuts+'.root')
commands.append('python HistoWeight.py -i TWminitree_QCDHT500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedQCDHT500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT500']))
commands.append('python HistoWeight.py -i TWminitree_QCDHT700_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedQCDHT700_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT700']))
commands.append('python HistoWeight.py -i TWminitree_QCDHT1000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedQCDHT1000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1000']))
commands.append('python HistoWeight.py -i TWminitree_QCDHT1500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedQCDHT1500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1500']))
commands.append('python HistoWeight.py -i TWminitree_QCDHT2000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedQCDHT2000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT2000']))

commands.append('hadd TWminitree_QCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/TWminitree_weightedQCDHT*_PSET_'+cuts+'.root')
commands.append('mv TWminitree_QCDHT*_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWminitree_QCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







