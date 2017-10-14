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
# parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
# 				  default	=	'on',
# 				  dest		=	'ptreweight',
# 				  help		=	'on or off')
# parser.add_option('--noExtraPtCorrection', metavar='F', action='store_false',
# 				  default=True,
# 				  dest='extraPtCorrection',
# 				  help='Call to turn off extraPtCorrection')
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

#Process multiple lumis at once with this code otherwise use the above constant pull from BstarFunctions
#lumiList = [1000, 5000, 10000]
#Lumi = ['1fb', '5fb', '10fb']


xsec_bsr = Cons['xsec_bsr']
xsec_bsl = Cons['xsec_bsl']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']
#nev_bsr = Cons['nev_bsr']
#nev_bsl = Cons['nev_bsl']
#nev_ttbar = Cons['nev_ttbar']
#nev_qcd = Cons['nev_qcd']
#nev_st = Cons['nev_st']
#nev_bpl = Cons['nev_bpl']

#----------------Need to set proper strings ---------------------------------
# We assume iterations = -1 (not running pt study)

# ptString should only be applied to ttbar 
# If we run with the extra correction
# ptString = ''
# if options.ptreweight == 'off':
# 	ptString = '_ptreweight_off'
# elif not options.extraPtCorrection:
# 	ptString = '_noExtraPtCorrection'

#-----------------------------------------------------------------------------

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

# ttbar
for ptString in ['','_noExtraPtCorrection','_ptreweight_off']:
	commands.append('rm rootfiles/'+Lumi+'/TWratefileweightedttbar_PSET_'+cuts+ptString+'.root')
	commands.append('python HistoWeight.py -i TWratefilettbar_PSET_'+cuts+ptString+'.root -o TWratefileweightedttbar_PSET_'+cuts+ptString+'.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
	commands.append('mv TWratefileweightedttbar_PSET_'+cuts+ptString+'.root rootfiles/'+Lumi+'/')
	commands.append('mv TWratefilettbar_PSET_'+cuts+ptString+'.root temprootfiles/')

# QCDHT
commands.append('rm rootfiles/'+Lumi+'/TWratefileQCD_PSET_'+cuts+'.root')
commands.append('python HistoWeight.py -i TWratefileQCDHT500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT500']))
commands.append('python HistoWeight.py -i TWratefileQCDHT700_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT700_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT700']))
commands.append('python HistoWeight.py -i TWratefileQCDHT1000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT1000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1000']))
commands.append('python HistoWeight.py -i TWratefileQCDHT1500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT1500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1500']))
commands.append('python HistoWeight.py -i TWratefileQCDHT2000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT2000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT2000']))

commands.append('hadd TWratefileQCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/TWratefileweightedQCDHT*_PSET_'+cuts+'.root')
commands.append('mv TWratefileQCDHT*_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWratefileQCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')


# Singletop
commands.append('rm rootfiles/'+Lumi+'/TWratefilesingletop_*_PSET_'+cuts+'.root')
#commands.append('python HistoWeight.py -i TWratefilesingletop_s_PSET_'+cuts+'.root -o TWratefilesingletop_s_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['S']))
commands.append('python HistoWeight.py -i TWratefilesingletop_t_PSET_'+cuts+'.root -o TWratefilesingletop_t_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['T']))
commands.append('python HistoWeight.py -i TWratefilesingletop_tB_PSET_'+cuts+'.root -o TWratefilesingletop_tB_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['TB']))
commands.append('python HistoWeight.py -i TWratefilesingletop_tW_PSET_'+cuts+'.root -o TWratefilesingletop_tW_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['TW']))
commands.append('python HistoWeight.py -i TWratefilesingletop_tWB_PSET_'+cuts+'.root -o TWratefilesingletop_tWB_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['TWB']))
commands.append('hadd TWratefilesingletop_PSET_'+cuts+'.root TWratefilesingletop_*_PSET_'+cuts+'weighted.root')
commands.append('mv TWratefilesingletop_*_PSET_'+cuts+'weighted.root rootfiles/'+Lumi+'/')
commands.append('mv TWratefilesingletop_*_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWratefilesingletop_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

# Data
commands.append('rm rootfiles/'+Lumi+'/TWratefiledata_PSET_'+cuts+'.root')
commands.append('mv TWratefiledata_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

#primeSigs = ['1200','1400','1600','1800']
#quark = ['B','T']
#for q in quark:
#        for sig in primeSigs:
#               commands.append('python HistoWeight.py -i TWratefileBprime'+q+'ToTW'+sig+'_PSET_'+cuts+'.root -o TWratefileBprime'+q+'ToTW'+sig+'_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_bpl[q+sig]))
#               commands.append('mv TWratefileBprime'+q+'ToTW'+sig+'_PSET_'+cuts+'weighted.root rootfiles/'+Lumi+'/')
#               commands.append('mv TWratefileBprime'+q+'ToTW'+sig+'_PSET_'+cuts+'.root temprootfiles/')

# Signals
for coup in ['LH','RH']:
	sigfiles = sorted(glob.glob('TWratefilesignal'+coup+'*_PSET_'+cuts+'.root'))
	for f in sigfiles:
#		print f
		mass = f.lstrip('TWratefilesignal'+coup).rstrip('_PSET_'+cuts+'.root')
		if coup == 'RH':
			xsec_sig = xsec_bsr[mass]
		elif coup == 'LH':
			xsec_sig = xsec_bsl[mass]
		commands.append('rm ' + f.replace('TWratefilesignal'+coup,'TWratefileweightedsignal'+coup))	 
		commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('TWratefilesignal'+coup,'TWratefileweightedsignal'+coup)+' -n auto -w ' + str(cLumi*xsec_sig))
		commands.append('mv '+f+' temprootfiles/')
		commands.append('mv '+f.replace('TWratefilesignal'+coup,'TWratefileweightedsignal'+coup)+' rootfiles/'+Lumi+'/')
for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







