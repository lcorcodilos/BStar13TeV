#! /usr/bin/env python
#BUILT FOR MULTIPLE LUMIS
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

var =''

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = [str(int(cLumi))+'pb']

xsec_ttbar = Cons['xsec_ttbar']

files = sorted(glob.glob("*job*of*.root"))

filestr = ['none','JES_up','JES_down','JER_up','JER_down','JMS_up','JMS_down','JMR_up','JMR_down']

pdfstr = ['pdf_up','pdf_down']
pilestr = ['pileup_up','pileup_down']

j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?)_PSET', f).group(1),""))

files_to_sum = list(set(j))

commands = []
commands.append('rm *.log') 
commands.append('rm temprootfiles/*.root')
commands.append('rm -rf notneeded')
for f in files_to_sum:
	commands.append('rm '+f) 
	commands.append('hadd ' + f + " " + f.replace('_PSET','_job*_PSET') )
	commands.append('mv ' +  f.replace('_PSET','_job*_PSET') + ' temprootfiles/')
	#commands.append('mv ' +  f + ' rootfiles/')




for l in range(len(lumiList)):
	lumi = lumiList[l]
	for scale in ['scaleup','scaledown']:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+'.root')
		commands.append('python HistoWeight.py -i TWanalyzerttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH'+scale]))
		commands.append('mv TWanalyzerttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	for f in filestr:
		ttbar_pustr = ''
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root temprootfiles/')
	for p in pdfstr:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root temprootfiles/')
	for p in pilestr:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+'.root temprootfiles/')



for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







