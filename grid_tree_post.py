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
# from optparse import OptionParser
import sys
from DataFormats.FWLite import Events, Handle


import Bstar_Functions	
from Bstar_Functions import *


# parser = OptionParser()

# parser.add_option('-a', '--alphabet', metavar='F', type='string', action='store',
# 				default       =       't',
# 				dest          =       'alphabet',
# 				help          =       'whether we want uncut t or w variables')

# (options, args) = parser.parse_args()


# print "Options summary"
# print "=================="
# for  opt,value in options.__dict__.items():
# 		#print str(option)+ ": " + str(options[option]) 
# 		print str(opt) +': '+ str(value)
# print "=================="
# print ""

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

filestr = ['none','pileup_up','pileup_down','JES_up','JES_down','JER_up','JER_down']

j = []
for f in files:
	j.append(f.replace('_jo'+re.search('_jo(.+?).root', f).group(1),""))

files_to_sum = list(set(j))

# Sum jobs
commands = []
commands.append('rm *.log') 
commands.append('rm -rf notneeded')
for f in files_to_sum:
	commands.append('rm '+f) 
	commands.append('hadd ' + f + " " + f.replace('.root','_job*.root') )
	commands.append('mv ' +  f.replace('.root','_job*.root') + ' tempTTrees/')


'''
executing python HistoWeight.py -i TWtreefile_ttbar.root -o TWtreefile_ttbarweighted.root -n auto -w 30292699.2
Traceback (most recent call last):
  File "HistoWeight.py", line 43, in <module>
    evweight = 1.0/float(events.Integral())
AttributeError: 'TObject' object has no attribute 'Integral'
'''

# ttbar
for f in filestr:
	commands.append('rm TTrees/TWtreefile_ttbar_Trigger_nominal_'+f+'.root')
	#commands.append('python HistoWeight.py -i TWtreefile_ttbar_Trigger_nominal_'+f+'.root -o TWtreefile_ttbar_Trigger_nominal_'+f+'_weighted.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
	commands.append('mv TWtreefile_ttbar_Trigger_nominal_'+f+'.root TTrees/')
	#commands.append('mv TWtreefile_ttbar_Trigger_nominal_'+f+'.root tempTTrees/')

# QCDHT
commands.append('rm TTrees/TWtreefile_QCD*_Trigger_nominal_none.root')
# commands.append('python HistoWeight.py -i TWtreefile_QCDHT500_Trigger_nominal_none.root -o TTrees/TWtreefile_QCDHT500_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT500']))
# commands.append('python HistoWeight.py -i TWtreefile_QCDHT700_Trigger_nominal_none.root -o TTrees/TWtreefile_QCDHT700_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT700']))
# commands.append('python HistoWeight.py -i TWtreefile_QCDHT1000_Trigger_nominal_none.root -o TTrees/TWtreefile_QCDHT1000_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT1000']))
# commands.append('python HistoWeight.py -i TWtreefile_QCDHT1500_Trigger_nominal_none.root -o TTrees/TWtreefile_QCDHT1500_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT1500']))
# commands.append('python HistoWeight.py -i TWtreefile_QCDHT2000_Trigger_nominal_none.root -o TTrees/TWtreefile_QCDHT2000_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT2000']))
#commands.append('hadd TWtreefile_QCD_Trigger_nominal_none.root TWtreefile_QCDHT*_Trigger_nominal_none.root ')
commands.append('mv TWtreefile_QCDHT*_Trigger_nominal_none.root TTrees/')
#commands.append('mv TWtreefile_QCDHT*_Trigger_nominal_none.root tempTTrees/')


# Singletop
commands.append('rm TTrees/TWtreefile_singletop_*_Trigger_nominal_none.root')
#commands.append('python HistoWeight.py -i TWtreefile_singletop_s_Trigger_nominal_none.root -o TTrees/TWtreefile_singletop_s_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_st['S']))
#commands.append('python HistoWeight.py -i TWtreefile_singletop_t_Trigger_nominal_none.root -o TTrees/TWtreefile_singletop_t_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_st['T']))
#commands.append('python HistoWeight.py -i TWtreefile_singletop_tB_Trigger_nominal_none.root -o TTrees/TWtreefile_singletop_tB_Trigger_nominal_none_weighted.root -n auto -w ' + str(cLumi*xsec_st['TB']))
#commands.append('python HistoWeight.py -i TWtreefile_singletop_tW.root -o TWtreefile_singletop_tWweighted.root -n auto -w ' + str(cLumi*xsec_st['TW']))
#commands.append('python HistoWeight.py -i TWtreefile_singletop_tWB.root -o TWtreefile_singletop_tWBweighted.root -n auto -w ' + str(cLumi*xsec_st['TWB']))
commands.append('mv TWtreefile_singletop_*_Trigger_nominal_none.root TTrees/')
#commands.append('mv TWtreefile_singletop_*_Trigger_nominal_none.root tempTTrees/')

# Data
commands.append('rm TTrees/TWtreefile_data_Trigger_nominal_none.root')
commands.append('mv TWtreefile_data_Trigger_nominal_none.root TTrees/TWtreefile_data_Trigger_nominal_none.root')


# Signals
for coup in ['LH','RH']:
	sigfiles = sorted(glob.glob('TWtreefile_signal'+coup+'*_Trigger_nominal_*.root'))
	for f in sigfiles:
#		print f
		# mass = f.lstrip('TWtreefile_signal'+coup).rstrip('.root')
		# if coup == 'RH':
		# 	xsec_sig = xsec_bsr[mass]
		# elif coup == 'LH':
		# 	xsec_sig = xsec_bsl[mass]
		#commands.append('rm ' + f.replace('.root','_weighted.root'))	 
		#commands.append('python HistoWeight.py -i '+f+' -o '+f.replace('.root','_weighted.root')+' -n auto -w ' + str(cLumi*xsec_sig))
		#commands.append('mv '+f+' tempTTrees/')
		#commands.append('mv '+f.replace('.root','_weighted.root')+' TTrees/')
		commands.append('mv '+f+' TTrees/')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







