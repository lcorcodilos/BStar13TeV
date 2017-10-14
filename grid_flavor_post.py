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

xsec_qcd = Cons['xsec_qcd']

commands = []

commands.append('rm rootfiles/'+Lumi+'/TWratefileQCD_PSET_'+cuts+'.root')
commands.append('python HistoWeight.py -i TWratefileQCDHT500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT500']))
commands.append('python HistoWeight.py -i TWratefileQCDHT700_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT700_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT700']))
commands.append('python HistoWeight.py -i TWratefileQCDHT1000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT1000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1000']))
commands.append('python HistoWeight.py -i TWratefileQCDHT1500_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT1500_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT1500']))
commands.append('python HistoWeight.py -i TWratefileQCDHT2000_PSET_'+cuts+'.root -o rootfiles/'+Lumi+'/TWratefileweightedQCDHT2000_PSET_'+cuts+'.root -n auto -w ' + str(cLumi*xsec_qcd['HT2000']))

commands.append('hadd TWratefileQCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/TWratefileweightedQCDHT*_PSET_'+cuts+'.root')
commands.append('mv TWratefileQCDHT*_PSET_'+cuts+'.root temprootfiles/')
commands.append('mv TWratefileQCD_PSET_'+cuts+'.root rootfiles/'+Lumi+'/')

for s in commands :
    print 'executing ' + s
    subprocess.call( [s], shell=True )
