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
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'pileup',
                  help		=	'If not data do pileup reweighting?')
parser.add_option('-i', '--iteration', metavar='F', type='int', action='store',
				  default	=	-1,
				  dest		=	'iteration',
				  help		=	'Scale factor iteration. Default 0')

 
(options, args) = parser.parse_args()

cuts = options.cuts

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
Lumi = str(int(cLumi))+'pb'


xsec_bsl = Cons['xsec_bsl']
xsec_bsr = Cons['xsec_bsr']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']

ptString = '_ptSF' + str(options.iteration)

files = sorted(glob.glob("*job*of*.root"))

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

# Data - needs propper iteration
commands.append('rm rootfiles/'+Lumi+'/TWanalyzerdata_Trigger_nominal_none_PSET_'+cuts+ptString+'.root')
commands.append('mv TWanalyzerdata_Trigger_nominal_none_PSET_'+cuts+ptString+'.root rootfiles/'+Lumi+'/')


# Singletop - needs propper iteration
# Start off weighting everything correctly
for st in ['tW', 'tWB', 't', 'tB']:
	stfiles = sorted(glob.glob('TWanalyzersingletop_'+st+'_Trigger_nominal_none_PSET_'+cuts+ptString+'.root'))
	for f in stfiles:
		xsec_ST = xsec_st[st.upper()]
		commands.append('rm ' + f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st))
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st)+' -n auto -w ' + str(cLumi*xsec_ST))
		commands.append('mv '+f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st)+' rootfiles/'+Lumi+'/')
		commands.append('mv '+f+' temprootfiles/')
# Now add the right stuff together (no pdf stuff here)
commands.append('rm rootfiles/'+Lumi+'/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_'+cuts+ptString+'.root')
commands.append('hadd rootfiles/'+Lumi+'/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_'+cuts+ptString+'.root rootfiles/'+Lumi+'/TWanalyzerweightedsingletop*_Trigger_nominal_none_PSET_'+cuts+ptString+'.root')


# Only make ttbar on zeroth iteration
# if options.iteration == 0:
	# Ttbar - extraPtCorrection_off
commands.append('rm rootfiles/'+Lumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+'_noExtraPtCorrection.root')
commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+'_noExtraPtCorrection.root -o rootfiles/'+Lumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+'_noExtraPtCorrection.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
commands.append('mv TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+'_noExtraPtCorrection.root temprootfiles/')
# else:
	# commands.append('rm rootfiles/'+Lumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+'_ptSF'+str(options.iteration)+'.root')
	# commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+'_ptSF'+str(options.iteration)+'.root -o rootfiles/'+Lumi+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+'_ptSF'+str(options.iteration)+'.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
	# commands.append('mv TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+'_ptSF'+str(options.iteration)+'.root temprootfiles/')

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







