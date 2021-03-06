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
                  default	=	'on',
                  dest		=	'var',
                  help		=	'blank or kinematics')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
                  default	=	'on',
                  dest		=	'pileup',
                  help		=	'If not data do pileup reweighting?')
parser.add_option('-t', '--ttsub', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'ttsub',
				  help		=	'on, off, or double')
parser.add_option('-q', '--justqcd', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'justqcd',
				  help		=	'on, off')
parser.add_option('-A', '--alphabet', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'alphabet',
				  help		=	'on, off')

 
(options, args) = parser.parse_args()

cuts = options.cuts

#TTbar subtraction string is set here
if options.ttsub == 'on':
	var = ''
elif options.ttsub == 'off':
	var = '_nottsub'
elif options.ttsub == 'double':
	var = '_doublettsub'

alphaString = ''
if options.alphabet == 'on':
	alphaString = 'alphabet_on'

mmstrList = ['',"_modm_up","_modm_down"]

pustr = ""
# if options.pileup == "off":
# 	pustr = "pileup_unweighted"
# elif options.pileup == "on":
	# pustr = "none"

import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
#Uncomment for the single lumi from BstarFunctions
cLumi = Cons['lumi']
lumiList = [cLumi]
Lumi = [str(int(cLumi))+'pb']


xsec_bsl = Cons['xsec_bsl']
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

filestr = ['none','JES_up','JES_down','JER_up','JER_down','JMS_up','JMS_down','JMR_up','JMR_down']

pdfstr = ['pdf_up','pdf_down']
pilestr = ['pileup_up','pileup_down']

j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?)_PSET', f).group(1),""))

files_to_sum = list(set(j))
print files_to_sum
commands = []
commands.append('rm *.log') 
commands.append('rm temprootfiles/*.root')
commands.append('rm -rf notneeded')
for f in files_to_sum:
	commands.append('rm '+f) 
	commands.append('hadd ' + f + " " + f.replace('_PSET','_job*_PSET') )
	commands.append('mv ' +  f.replace('_PSET','_job*_PSET') + ' temprootfiles/')
	#commands.append('mv ' +  f + ' rootfiles/')

if options.ttsub == 'on' or options.ttsub == 'off':
	for l in range(len(lumiList)):
		lumi = lumiList[l]
		for mmstr in mmstrList:
			commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerQCD_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root')
			commands.append('python HistoWeight.py -i TWanalyzerQCDHT500_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT500_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -n auto -w ' + str(lumi*xsec_qcd['HT500']))
			commands.append('python HistoWeight.py -i TWanalyzerQCDHT700_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT700_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -n auto -w ' + str(lumi*xsec_qcd['HT700']))
			commands.append('python HistoWeight.py -i TWanalyzerQCDHT1000_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT1000_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -n auto -w ' + str(lumi*xsec_qcd['HT1000']))
			commands.append('python HistoWeight.py -i TWanalyzerQCDHT1500_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT1500_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -n auto -w ' + str(lumi*xsec_qcd['HT1500']))
			commands.append('python HistoWeight.py -i TWanalyzerQCDHT2000_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT2000_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root -n auto -w ' + str(lumi*xsec_qcd['HT2000']))

			commands.append('hadd TWanalyzerQCD_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root rootfiles/'+Lumi[l]+'/TWanalyzerweightedQCDHT*_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root')
			commands.append('mv TWanalyzerQCD_Trigger_nominal_'+filestr[0]+mmstr+'_PSET_'+cuts+alphaString+'.root rootfiles/'+Lumi[l]+'/')

	commands.append('mv TWanalyzerQCDHT*_Trigger_nominal_*_PSET_'+cuts+alphaString+'.root temprootfiles/')

if options.justqcd == 'on':
	for s in commands :
		print 'executing ' + s
		subprocess.call( [s], shell=True )
	quit()

for l in range(len(lumiList)):
	lumi = lumiList[l]
	for scale in ['scaleup','scaledown']:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root')
		commands.append('python HistoWeight.py -i TWanalyzerttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH'+scale]))
		commands.append('mv TWanalyzerttbar'+scale+'_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	for f in filestr:
		ttbar_pustr = ''
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+mmstrList[0]+ttbar_pustr+'_PSET_'+cuts+var+alphaString+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_'+f+mmstrList[0]+ttbar_pustr+'_PSET_'+cuts+var+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_'+f+mmstrList[0]+ttbar_pustr+'_PSET_'+cuts+var+alphaString+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_'+f+mmstrList[0]+ttbar_pustr+'_PSET_'+cuts+var+alphaString+'.root temprootfiles/')
	for p in pdfstr:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root temprootfiles/')
	for p in pilestr:
		commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root') #removes old file with same name in /rootfiles/
		commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
		commands.append('mv TWanalyzerttbar_Trigger_nominal_none_'+p+'_PSET_'+cuts+var+alphaString+'.root temprootfiles/')
	# if options.cuts == 'sideband1':
	if options.ttsub == 'on':
		for p in ['_noExtraPtCorrection','_ptreweight_off']:
			commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+p+alphaString+'.root')
			commands.append('python HistoWeight.py -i TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+p+alphaString+'.root -o rootfiles/'+Lumi[l]+'/TWanalyzerweightedttbar_Trigger_nominal_none_PSET_'+cuts+p+alphaString+'.root -n auto -w ' + str(lumi*xsec_ttbar['PH']))
			commands.append('mv TWanalyzerttbar_Trigger_nominal_none_PSET_'+cuts+p+alphaString+'.root temprootfiles/')

for l in range(len(lumiList)):
	lumi = lumiList[l]
	commands.append('rm rootfiles/'+Lumi[l]+'/TWanalyzerdata_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+filestr[0]+'_PSET_'+cuts+var+alphaString+'.root rootfiles/'+Lumi[l]+'/')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+filestr[0]+'_modm_down_PSET_'+cuts+var+alphaString+'.root rootfiles/'+Lumi[l]+'/')
	commands.append('mv TWanalyzerdata_Trigger_nominal_'+filestr[0]+'_modm_up_PSET_'+cuts+var+alphaString+'.root rootfiles/'+Lumi[l]+'/')
	

#primeSigs = ['1200','1400','1600','1800']
#quark = ['B','T']
#for q in quark:
#        for sig in primeSigs:
#		for f in filestr:
#			commands.append('rm rootfiles/'+Lumi[0]+'/TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'weighted.root')
#			commands.append('python HistoWeight.py -i TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+alphaString+'.root -o rootfiles/'+Lumi[0]+'/TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+'weighted.root -n auto -w ' + str(cLumi*xsec_bpl[q+sig]))
#			commands.append('mv TWanalyzerBprime'+q+'ToTW'+sig+'_Trigger_nominal_'+f+'_PSET_'+cuts+var+alphaString+'.root temprootfiles/')


for coup in ['LH','RH']:
	sigfiles = sorted(glob.glob('TWanalyzersignal'+coup+'*_PSET_'+cuts+var+alphaString+'.root'))
	for f in sigfiles:
		mass = f[18:22]#.lstrip('TWanalyzersignal'+coup).rstrip('_Trigger_nominal_'+g+'_PSET_'+cuts+alphaString+'.root')
		if coup == 'RH':
			xsec_sig = xsec_bsr[mass]
		elif coup == 'LH':
			xsec_sig = xsec_bsl[mass]
		commands.append('rm ' + f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup))
		for l in range(len(lumiList)):
			lumi = lumiList[l]	 
			commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' -n auto -w ' + str(lumi*xsec_sig))
			commands.append('mv '+f.replace('TWanalyzersignal'+coup,'TWanalyzerweightedsignal'+coup)+' rootfiles/'+Lumi[l]+'/')
		commands.append('mv '+f+' temprootfiles/')

# Create vector like signals
#commands.append('cd rootfiles/'+Lumi[l])
#commands.append('python MakeVectorLike.py -c ' + cuts)
#commands.append('cd ../../')


# Singletop

# Start off weighting everything correctly
for st in ['tW', 'tWB', 't', 'tB']:
	stfiles = sorted(glob.glob('TWanalyzersingletop_'+st+'_*_PSET_'+cuts+var+alphaString+'.root'))
	for f in stfiles:
		xsec_ST = xsec_st[st.upper()]
		commands.append('rm ' + f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st))
		for l in range(len(lumiList)):
			lumi = lumiList[l]
			commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st)+' -n auto -w ' + str(lumi*xsec_ST))
			commands.append('mv '+f.replace('TWanalyzersingletop_'+st,'TWanalyzerweightedsingletop_'+st)+' rootfiles/'+Lumi[l]+'/')
		commands.append('mv '+f+' temprootfiles/')


# Now add the right stuff together (no pdf stuff here)
for l in Lumi:
	for f in filestr:	
		commands.append('rm rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+f+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root')
		commands.append('hadd rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+f+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root rootfiles/'+l+'/TWanalyzerweightedsingletop*_Trigger_nominal_'+f+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root')


# for st in stfiles:
# 	channel = f.replace('TWanalyzersingletop_','').replace('_Trigger_nominal_'+pustr+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root','')
# 	xsec_ST = xsec_st[channel.upper()]
# 	commands.append('rm ' + f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_'))
# 	for l in range(len(lumiList)):	
# 		lumi = lumiList[l] 
# 		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' -n auto -w ' + str(lumi*xsec_ST))
# 		commands.append('mv '+f.replace('TWanalyzersingletop_','TWanalyzerweightedsingletop_')+' rootfiles/'+Lumi[l]+'/')
# 	commands.append('mv '+f+' temprootfiles/')
# for l in Lumi:
# 	commands.append('rm rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+pustr+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root')
# 	commands.append('hadd rootfiles/'+l+'/TWanalyzerweightedsingletop_Trigger_nominal_'+pustr+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root rootfiles/'+l+'/TWanalyzerweightedsingletop*_Trigger_nominal_'+pustr+mmstrList[0]+'_PSET_'+cuts+var+alphaString+'.root')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







