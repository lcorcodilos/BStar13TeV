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
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
                  default	=	'nominal',
                  dest		=	'modmass',
                  help		=	'nominal up or down')
 
(options, args) = parser.parse_args()

cuts = options.cuts
var = ''
if options.var=='kinematics':
	var = '_kin'
mmstr = ""
#if options.modmass!="nominal":
#	print "using modm uncertainty"
#	mmstr = "_modm_"+options.modmass


import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = [str(int(cLumi))+'pb']
if options.cuts == 'default':
	wtagsf = Cons['wtagsf_HP']
	wtagsfsig = Cons['wtagsfsig_HP']
elif options.cuts == 'sideband':
	wtagsf = Cons['wtagsf_LP']
	wtagsfsig = Cons['wtagsfsig_LP']
xsec_bsr = Cons['xsec_bsr']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']
#nev_bsl = Cons['nev_bsl']
#nev_ttbar = Cons['nev_ttbar']
#nev_qcd = Cons['nev_qcd']
#nev_st = Cons['nev_st']
#nev_bpl = Cons['nev_bpl']

#Process multiple lumis at once with this code otherwise use the above constant pull from BstarFunctions
#lumiList = [1000, 5000, 10000]
#Lumi = ['1fb', '5fb', '10fb']

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


for l in range(len(lumiList)):
	lumi = lumiList[l]
	commands.append('rm rootfiles/'+Lumi[l]+'/TWvariablesQCD_Trigger_nominal_none'+mmstr+'_PSET_rate_default.root')
	commands.append('python HistoWeight.py -i TWvariablesQCDHT500_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWvariablesQCDHT500_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT500']))
	commands.append('python HistoWeight.py -i TWvariablesQCDHT700_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWvariablesQCDHT700_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT700']))
	commands.append('python HistoWeight.py -i TWvariablesQCDHT1000_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWvariablesQCDHT1000_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT1000']))
	commands.append('python HistoWeight.py -i TWvariablesQCDHT1500_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWvariablesQCDHT1500_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT1500']))
	commands.append('python HistoWeight.py -i TWvariablesQCDHT2000_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWvariablesQCDHT2000_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT2000']))

	commands.append('hadd TWvariablesQCD_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root temprootfiles/TWvariablesQCDHT*_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+'weighted.root')
	commands.append('mv TWvariablesQCD_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')

commands.append('mv TWvariablesQCDHT*_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root temprootfiles/')


for l in range(len(lumiList)):
	lumi = lumiList[l]
	commands.append('rm rootfiles/'+Lumi[l]+'/TWvariablesweightedttbar_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root') #removes old file with same name in /rootfiles/
	commands.append('python HistoWeight.py -i TWvariablesttbar_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWvariablesweightedttbar_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
	commands.append('mv TWvariablesttbar_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	commands.append('rm rootfiles/'+Lumi[l]+'/TWvariablesdata_Trigger_nominal_none_PSET_'+cuts+var+'.root')
	commands.append('mv TWvariablesdata_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	#commands.append('mv TWvariablesdata_Trigger_nominal_none_modm_down_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	#commands.append('mv TWvariablesdata_Trigger_nominal_none_modm_up_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	

#primeSigs = ['1200','1400','1600','1800']
#quark = ['B','T']
#for q in quark:
#        for sig in primeSigs:
#		commands.append('rm rootfiles/'+Lumi[0]+'/TWvariablesBprime'+q+'ToTW'+sig+'_Trigger_nominal_PSET_'+cuts+var+'weighted.root -n auto')
#		commands.append('python HistoWeight.py -i TWvariablesBprime'+q+'ToTW'+sig+'_Trigger_nominal_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[0]+'/TWvariablesBprime'+q+'ToTW'+sig+'_Trigger_nominal_PSET_'+cuts+var+'weighted.root -n auto -w ' + str(cLumi*xsec_bpl[q+sig]/nev_bpl[q+sig]))
#		commands.append('mv TWvariablesBprime'+q+'ToTW'+sig+'_Trigger_nominalface_PSET_'+cuts+var+'.root temprootfiles/')


for coup in ['RH']:#,'LH']:
	sigfiles = sorted(glob.glob('TWvariablessignal'+coup+'*_PSET_'+cuts+var+'.root'))
	for f in sigfiles:
		mass = f[19:23]#.lstrip('TWvariablessignal'+coup).rstrip('_Trigger_nominal_'+g+'_PSET_'+cuts+'.root')
		if coup == 'RH':
			xsec_sig = xsec_bsr[mass]
		elif coup == 'LH':
			xsec_sig = xsec_bsl[mass]
		commands.append('rm ' + f.replace('TWvariablessignal'+coup,'TWvariablesweightedsignal'+coup))
		for l in range(len(lumiList)):
			lumi = lumiList[l]	 
			commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWvariablessignal'+coup,'TWvariablesweightedsignal'+coup)+' -n auto -w ' + str(lumi*wtagsf*xsec_sig))
			commands.append('mv '+f.replace('TWvariablessignal'+coup,'TWvariablesweightedsignal'+coup)+' rootfiles/'+Lumi[l]+'/')
		commands.append('mv '+f+' temprootfiles/')



stfiles = ['TWvariablessingletop_t_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root',
		'TWvariablessingletop_tB_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root',
		'TWvariablessingletop_tW_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root',
                'TWvariablessingletop_tWB_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root']

for f in stfiles:
	channel = f.replace('TWvariablessingletop_','').replace('_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root','')
	xsec_ST = xsec_st[channel.upper()]
	#nev_ST = nev_st[channel.upper()]
	commands.append('rm ' + f.replace('TWvariablessingletop_','TWvariablesweightedsingletop_'))
	for l in range(len(lumiList)):	
		lumi = lumiList[l] 
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWvariablessingletop_','TWvariablesweightedsingletop_')+' -n auto -w ' + str(lumi*xsec_ST))
		commands.append('mv '+f.replace('TWvariablessingletop_','TWvariablesweightedsingletop_')+' rootfiles/'+Lumi[l]+'/')
	commands.append('mv '+f+' temprootfiles/')
for l in Lumi:
	commands.append('rm rootfiles/'+l+'/TWvariablesweightedsingletop_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root')
	commands.append('hadd rootfiles/'+l+'/TWvariablesweightedsingletop_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root rootfiles/'+l+'/TWvariablesweightedsingletop*_Trigger_nominal_none'+mmstr+'_PSET_'+cuts+var+'.root')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







