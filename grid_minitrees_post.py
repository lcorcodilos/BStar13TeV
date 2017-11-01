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

# ttbar
for ptString in ['']:#,'_noExtraPtCorrection','_ptreweight_off']:
	commands.append('rm rootfiles/'+Lumi+'/TWminitree_weightedttbar_PSET_'+cuts+ptString+'.root')
	commands.append('python HistoWeight.py -i TWminitree_ttbar_PSET_'+cuts+ptString+'.root -o TWminitree_weightedttbar_PSET_'+cuts+ptString+'.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
	commands.append('mv TWminitree_weightedttbar_PSET_'+cuts+ptString+'.root rootfiles/'+Lumi+'/')
	commands.append('mv TWminitree_ttbar_PSET_'+cuts+ptString+'.root temprootfiles/')


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

# Singletop
commands.append('rm rootfiles/'+Lumi+'/TWminitree_singletop_*_PSET_'+cuts+'.root')
#commands.append('python HistoWeight.py -i TWminitree_singletop_s_PSET_'+cuts+'.root -o TWminitree_singletop_s_PSET_'+cuts+'weighted.root -n auto -w ' + str(cLumi*xsec_st['S']))
commands.append('python HistoWeight.py -i TWminitree_singletop_t_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedsingletop_t_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_st['T']))
commands.append('python HistoWeight.py -i TWminitree_singletop_tB_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedsingletop_tB_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_st['TB']))
commands.append('python HistoWeight.py -i TWminitree_singletop_tW_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedsingletop_tW_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_st['TW']))
commands.append('python HistoWeight.py -i TWminitree_singletop_tWB_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWminitree_weightedsingletop_tWB_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_st['TWB']))
commands.append('hadd TWminitree_singletop_PSET_'+cuts+'.root rootfiles/'+Lumi+'/TWminitree_weightedsingletop_*_PSET_'+cuts+'.root')
commands.append('mv TWminitree_singletop_*_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWminitree_singletop_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

# Data
commands.append('rm rootfiles/'+Lumi+'/TWminitree_data_PSET_'+cuts+'.root')
commands.append('mv TWminitree_data_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')


for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







