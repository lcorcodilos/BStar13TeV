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

files = sorted(glob.glob("*job*of*.root"))

j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?)_PSET', f).group(1),""))

files_to_sum = list(set(j))

commands = []
commands.append('rm *.log') 
#commands.append('rm temprootfiles/*.root')
commands.append('rm -rf notneeded')
for f in files_to_sum:
	commands.append('rm '+f) 
	commands.append('hadd ' + f + " " + f.replace('_PSET','_job*_PSET') )
	commands.append('mv ' +  f.replace('_PSET','_job*_PSET') + ' temprootfiles/')
	#commands.append('mv ' +  f + ' rootfiles/')



commands.append('rm rootfiles/TWkinematicsQCD_Trigger_nominal_none_PSET_rate_default.root')
commands.append('python HistoWeight.py -i TWkinematicsQCDPT300_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT300_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['300']/nev_qcd['300']))
commands.append('python HistoWeight.py -i TWkinematicsQCDPT470_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT470_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['470']/nev_qcd['470']))
commands.append('python HistoWeight.py -i TWkinematicsQCDPT600_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT600_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['600']/nev_qcd['600']))
commands.append('python HistoWeight.py -i TWkinematicsQCDPT800_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT800_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['800']/nev_qcd['800']))
commands.append('python HistoWeight.py -i TWkinematicsQCDPT1000_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT1000_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['1000']/nev_qcd['1000']))
commands.append('python HistoWeight.py -i TWkinematicsQCDPT1400_Trigger_nominal_none_PSET_'+cuts+'.root -o temprootfiles/TWkinematicsQCDPT1400_Trigger_nominal_none_PSET_'+cuts+'weighted.root -w ' + str(lumi*xsec_qcd['1400']/nev_qcd['1400']))
commands.append('hadd TWkinematicsQCD_Trigger_nominal_none_PSET_'+cuts+'.root temprootfiles/TWkinematicsQCDPT*_Trigger_nominal_none_PSET_'+cuts+'weighted.root')
commands.append('mv TWkinematicsQCDPT*_Trigger_nominal_none_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWkinematicsQCD_Trigger_nominal_none_PSET_'+cuts+'.root rootfiles/')


commands.append('rm rootfiles/TWkinematicsweightedttbar_Trigger_nominal_none_PSET_'+cuts+'.root')
commands.append('python HistoWeight.py -i TWkinematicsttbar_Trigger_nominal_none_PSET_'+cuts+'.root -o TWkinematicsweightedttbar_Trigger_nominal_none_PSET_'+cuts+'.root -w ' + str(lumi*xsec_ttbar['MG']/nev_ttbar['MG']))
commands.append('mv TWkinematicsweightedttbar_Trigger_nominal_none_PSET_'+cuts+'.root rootfiles/')
commands.append('mv TWkinematicsttbar_Trigger_nominal_none_PSET_'+cuts+'.root temprootfiles/')





for coup in ['right','left']:
	sigfiles = sorted(glob.glob('TWkinematicssignal'+coup+'*_PSET_'+cuts+'.root'))
	for f in sigfiles:
		mass = f.replace('TWkinematicssignal'+coup,'')[:4].replace("_","")
		xsec_sig = xsec_bsr[mass]
		if coup =='right':
			nev_sig = nev_bsr[mass]
		if coup =='left':
			nev_sig = nev_bsl[mass]
	
		commands.append('rm ' + f.replace('TWkinematicssignal'+coup,'TWkinematicsweightedsignal'+coup))	 
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWkinematicssignal'+coup,'TWkinematicsweightedsignal'+coup)+' -w ' + str(lumi*xsec_sig*ttagsf*wtagsf/nev_sig))
		commands.append('mv '+f+' temprootfiles/')
		commands.append('mv '+f.replace('TWkinematicssignal'+coup,'TWkinematicsweightedsignal'+coup)+' rootfiles/')


stfiles = sorted(glob.glob('TWkinematicssingletop_*_Trigger_nominal_none_PSET_'+cuts+'.root'))

for f in stfiles:
	print f
	channel = f.replace('TWkinematicssingletop_','').replace('_Trigger_nominal_none_PSET_'+cuts+'.root','')
	print channel
	xsec_ST = xsec_st[channel]
	nev_ST = nev_st[channel]
	commands.append('rm ' + f.replace('TWkinematicssingletop_','TWkinematicsweightedsingletop_'))	 
	commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWkinematicssingletop_','TWkinematicsweightedsingletop_')+' -w ' + str(lumi*xsec_ST*ttagsf*wtagsf/nev_ST))
	commands.append('mv '+f+' temprootfiles/')
	commands.append('mv '+f.replace('TWkinematicssingletop_','TWkinematicsweightedsingletop_')+' rootfiles/')



for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







