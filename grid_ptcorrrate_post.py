#! /usr/bin/env python
#NOT BUILT FOR MULTIPLE LUMIS

# --------------------------------------------------------------- #
# Not used for 
# --------------------------------------------------------------- #


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
                  default	=	'rate_sideband1',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-i', '--iteration', metavar='F', type='int', action='store',
				  default	=	0,
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
lumiList = [cLumi]
Lumi = str(int(cLumi))+'pb'

wtagsf = Cons['wtagsf_LP']
wtagsfsig = Cons['wtagsfsig_LP']
xsec_bsr = Cons['xsec_bsr']
xsec_bsl = Cons['xsec_bsl']
xsec_ttbar = Cons['xsec_ttbar']
xsec_qcd = Cons['xsec_qcd']
xsec_st = Cons['xsec_st']
xsec_bpl = Cons['xsec_bpl']

if options.iteration == 0:
	ptString = '_noExtraPtCorrection'
else:
	ptString = '_ptSF' + str(options.iteration)


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

# ttbar - needs propper SF iteration
commands.append('rm rootfiles/TWratefileweightedttbar_PSET_'+cuts+ptString+'.root')
commands.append('python HistoWeight.py -i TWratefilettbar_PSET_'+cuts+ptString+'.root -o TWratefileweightedttbar_PSET_'+cuts+ptString+'.root -n auto -w ' + str(cLumi*xsec_ttbar['PH']))
commands.append('mv TWratefileweightedttbar_PSET_'+cuts+ptString+'.root rootfiles/'+Lumi+'/')
commands.append('mv TWratefilettbar_PSET_'+cuts+ptString+'.root temprootfiles/')

# Only make data and singletop on zeroth iteration
if options.iteration == 0:
	# Singletop
	commands.append('rm rootfiles/'+Lumi+'/TWratefilesingletop_*_PSET_'+cuts+'.root')
	commands.append('python HistoWeight.py -i TWratefilesingletop_t_PSET_'+cuts+'.root -o TWratefilesingletop_t_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_st['T']))
	commands.append('python HistoWeight.py -i TWratefilesingletop_tB_PSET_'+cuts+'.root -o TWratefilesingletop_tB_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_st['TB']))
	commands.append('python HistoWeight.py -i TWratefilesingletop_tW_PSET_'+cuts+'.root -o TWratefilesingletop_tW_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_st['TW']))
	commands.append('python HistoWeight.py -i TWratefilesingletop_tWB_PSET_'+cuts+'.root -o TWratefilesingletop_tWB_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_st['TWB']))
	commands.append('hadd TWratefilesingletop_PSET_'+cuts+'.root TWratefilesingletop_*_PSET_'+cuts+'_weighted.root')
	commands.append('mv TWratefilesingletop_*_PSET_'+cuts+'_weighted.root rootfiles/'+Lumi+'/')
	commands.append('mv TWratefilesingletop_*_PSET_'+cuts+'.root temprootfiles/')
	commands.append('mv TWratefilesingletop_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

	# Data
	commands.append('rm rootfiles/'+Lumi+'/TWratefiledata_PSET_'+cuts+'.root')
	commands.append('mv TWratefiledata_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

	# QCDHT
	commands.append('rm rootfiles/'+Lumi+'/TWratefileQCD_PSET_'+cuts+'.root')
	commands.append('python HistoWeight.py -i TWratefileQCDHT500_PSET_'+cuts+'.root -o temprootfiles/TWratefileQCDHT500_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT500']))
	commands.append('python HistoWeight.py -i TWratefileQCDHT700_PSET_'+cuts+'.root -o temprootfiles/TWratefileQCDHT700_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT700']))
	commands.append('python HistoWeight.py -i TWratefileQCDHT1000_PSET_'+cuts+'.root -o temprootfiles/TWratefileQCDHT1000_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT1000']))
	commands.append('python HistoWeight.py -i TWratefileQCDHT1500_PSET_'+cuts+'.root -o temprootfiles/TWratefileQCDHT1500_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT1500']))
	commands.append('python HistoWeight.py -i TWratefileQCDHT2000_PSET_'+cuts+'.root -o temprootfiles/TWratefileQCDHT2000_PSET_'+cuts+'_weighted.root -n auto -w ' + str(cLumi*xsec_qcd['HT2000']))

	commands.append('hadd TWratefileQCD_PSET_'+cuts+'.root temprootfiles/TWratefileQCDHT*_PSET_'+cuts+'_weighted.root')
	commands.append('mv TWratefileQCDHT*_PSET_'+cuts+'.root temprootfiles/')
	commands.append('mv TWratefileQCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )







