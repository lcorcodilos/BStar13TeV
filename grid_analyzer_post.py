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
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'pileup',
                  help		=	'If not data do pileup reweighting?')

 
(options, args) = parser.parse_args()

cuts = options.cuts
var = ''
if options.var=='kinematics':
	var = '_kin'

mmstrList = ["","_modm_up","_modm_down"]

pustr = ""
if options.pileup == "off":
	pustr = "pileup_unweighted"
elif options.pileup == "on":
	pustr = "none"

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = [str(int(cLumi))+'pb']

wtagsf = Cons['wtagsf']
wtagsfsig = Cons['wtagsfsig']
xsec_bsl = Cons['xsec_bsl']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']
nev_bsl = Cons['nev_bsl']
nev_ttbar = Cons['nev_ttbar']
nev_qcd = Cons['nev_qcd']
nev_st = Cons['nev_st']
nev_bpl = Cons['nev_bpl']

#Process multiple lumis at once with this code otherwise use the above constant pull from BstarFunctions
#lumiList = [1000, 5000, 10000]
#Lumi = ['1fb', '5fb', '10fb']

files = sorted(glob.glob("*job*of*.root"))

filestr = ['none','pileup_up','pileup_down','JES_up','JES_down','JER_up','JER_down']


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
	for mmstr in mmstrList:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_rate_default.root')
		commands.append('python HistoWeight.py -i TWanalyzerQCDHT500_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDHT500_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT500']))
		commands.append('python HistoWeight.py -i TWanalyzerQCDHT700_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDHT700_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT700']))
		commands.append('python HistoWeight.py -i TWanalyzerQCDHT1000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDHT1000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT1000']))
		commands.append('python HistoWeight.py -i TWanalyzerQCDHT1500_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDHT1500_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT1500']))
		commands.append('python HistoWeight.py -i TWanalyzerQCDHT2000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDHT2000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['HT2000']))

		commands.append('hadd TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root temprootfiles/TWanalyzerQCDHT*_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root')
		commands.append('mv TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')

commands.append('mv TWanalyzerQCDHT*_Trigger_nominal_*_PSET_'+cuts+var+'.root temprootfiles/')

# QCDPT
#for l in range(len(lumiList)):
#	lumi = lumiList[l]
#	for mmstr in mmstrList:
#		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_rate_default.root')
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT300_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT300_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT300']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT470_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT470_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT470']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT600_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT600_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT600']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT800_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT800_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT800']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT1000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT1000_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT1000']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT1400_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT1400_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT1400']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT1800_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT1800_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT1800']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT2400_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT2400_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT2400']))
#		commands.append('python HistoWeight.py -i TWanalyzerQCDPT3200_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root -o temprootfiles/TWanalyzerQCDPT3200_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(lumi*xsec_qcd['PT3200']))

#		commands.append('hadd TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root temprootfiles/TWanalyzerQCDPT*nominal_'+pustr+mmstr+'_PSET_'+cuts+'weighted.root')
#		commands.append('mv TWanalyzerQCD_Trigger_nominal_'+pustr+mmstr+'_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')

#commands.append('mv TWanalyzerQCDPT*_Trigger_nominal_*_PSET_'+cuts+var+'.root temprootfiles/')

#for l in range(len(lumiList)):
#	lumi = lumiList[l]
#	for scale in ['scaleup','scaledown']:
#		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root')
#		commands.append('python HistoWeight.py -i TWanalyzerttbar'+scale+'_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*wtagsf*xsec_ttbar['PH'+scale]))
#		commands.append('mv TWanalyzerttbar'+scale+'_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	for f in filestr:
		ttbar_pustr = ''
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root -n auto -w ' + str(lumi*wtagsf*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_'+f+ttbar_pustr+'_PSET_'+cuts+var+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerdata_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+pustr+'_modm_down_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+pustr+'_modm_up_PSET_'+cuts+var+'.root rootfiles/'+Lumi[l]+'/')
	

#primeSigs = ['1200','1400','1600','1800']
#quark = ['B','T']
#for q in quark:
#        for sig in primeSigs:
#		for f in filestr:
#			commands.append('rm rootfiles/'+Lumi[0]+'/TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'weighted.root')
#			commands.append('python HistoWeight.py -i TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'.root -o rootfiles/'+Lumi[0]+'/TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'weighted.root -n auto -w ' + str(cLumi*xsec_bpl[q+sig]))
#			commands.append('mv TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'.root temprootfiles/')


for coup in ['LH','RH']:
	sigfiles = sorted(glob.glob('TWanalyzersignal'+coup+'*_PSET_'+cuts+var+'.root'))
	for f in sigfiles:
		mass = f[18:22]#.lstrip('TWanalyzersignal'+coup).rstrip('_Trigger_nominal_'+g+'_PSET_'+cuts+'.root')
		if coup == 'RH':
			xsec_sig = xsec_bsr[mass]
		elif coup == 'LH':
			xsec_sig = xsec_bsl[mass]
		commands.append('rm ' + f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup))
		for l in range(len(lumiList)):
			lumi = lumiList[l]	 
			commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' -n auto -w ' + str(lumi*wtagsfsig*xsec_sig))
			commands.append('mv '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' rootfiles/'+Lumi[l]+'/')
		commands.append('mv '+f+' temprootfiles/')



stfiles = [	'TWanalyzersingletop_s_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root',
		'TWanalyzersingletop_t_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root',
		'TWanalyzersingletop_tB_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root']

for f in stfiles:
	channel = f.replace('TWanalyzersingletop_','').replace('_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root','')
	xsec_ST = xsec_st[channel.upper()]
	commands.append('rm ' + f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_'))
	for l in range(len(lumiList)):	
		lumi = lumiList[l] 
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' -n auto -w ' + str(lumi*xsec_ST*wtagsf))
		commands.append('mv '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' rootfiles/'+Lumi[l]+'/')
	commands.append('mv '+f+' temprootfiles/')
for l in Lumi:
	commands.append('rm rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root')
	commands.append('hadd rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root rootfiles/'+l+'/TWanalyzerweightedsingletop*_Trigger_nominal_'+pustr+'_PSET_'+cuts+var+'.root')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







