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
parser.add_option('-v', '--var', metavar='F', type='string', action='store',
                  default	=	'',
                  dest		=	'var',
                  help		=	'blank or kinematics')
(options, args) = parser.parse_args()

cuts = options.cuts
var = ''
if options.var=='kinematics':
	var = 'kin'

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = [str(int(cLumi))+'pb']

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

#Process multiple lumis at once with this code otherwise use the above constant pull from BstarFunctions
#lumiList = [1000, 5000, 10000]
#Lumi = ['1fb', '5fb', '10fb']

commands = []

stfiles = [	'TWanalyzersingletop_s_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root',
		'TWanalyzersingletop_t_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root',
		'TWanalyzersingletop_tW_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root',
		'TWanalyzersingletop_tWB_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root']

for f in stfiles:
	print f
	channel = f.replace('TWanalyzersingletop_','').replace('_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root','')
	print channel.upper()
	xsec_ST = xsec_st[channel.upper()]
	nev_ST = nev_st[channel.upper()]
	commands.append('rm ' + f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_'))
	for l in range(len(lumiList)):	
		lumi = lumiList[l] 
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' -w ' + str(lumi*xsec_ST*ttagsf*wtagsf/nev_ST))
		commands.append('mv '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' rootfiles/'+Lumi[l]+'/')
	commands.append('mv '+f+' temprootfiles/')
for l in Lumi:
	commands.append('hadd rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root rootfiles/'+l+'/TWanalyzerweightedsingletop*_Trigger_nominal_none_PSET_'+cuts+'_'+var+'.root')

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







