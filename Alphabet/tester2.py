# TEST AREA
import os
# import sys
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy
from optparse import OptionParser

# Our Bstar.Fit.fittions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *
import Alphabet
from Alphabet import *
# sys.path.append("..")
# import Bstar_Functions
# from Bstar_Functions import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				default       =       'data',
				dest          =       'set',
				help          =       'data or QCD')

(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
		#print str(option)+ ": " + str(options[option]) 
		print str(opt) +': '+ str(value)
print "=================="
print ""

# Cons = LoadConstants()
# lumi = Cons['lumi']
lumi = str(36.420)

### DEFINE THE DISTRIBUTIONS YOU WANT TO USE:

# DISTRIBUTIONS YOU WANT TO ESTIMATE:

# FORMAT IS:
# dist = ("name", "location of file", "name of tree", "weight (can be more complicated than just a number, see MC example below)")
if options.set == "data":
	Data = DIST("Data", "TWtreefile_data.root", "Tree", "weight")
elif options.set == "QCD":
	Data = DIST("QCD", "TWtreefile_QCD.root", "Tree", "weight")
# DISTRIBUTIONS YOU NEED TO SUBTRACT (KNOWN MC CONTRIBUTIONS):
ttbar = DIST("ttbar", "TWtreefile_ttbarweighted.root", "Tree", "weight")
singletop = DIST("st", "TWtreefile_singletop.root", "Tree", "weight")

DistsWeWantToEstiamte = [Data]
DistsWeWantToIgnore = [ttbar, singletop]

# Before proceeding, need to reweight our dists to cross section, lumi, and number of events
# The weighting for this is stored in the TWtreefile, just need to grab and apply using the below
# function from Distribution_Header.py -LC 3/20/17

# Only want to do this with MC since data doesn't get this weight
if options.set == "QCD":
	Data.bstarReweight()
for distI in DistsWeWantToIgnore:
	distI.bstarReweight()