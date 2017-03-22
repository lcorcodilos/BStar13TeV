import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

# Our functions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *

myFile = ROOT.TFile("TWtreefile_ttbarweighted.root")
myTree = myFile.Get("Tree")
wmassBranch = myTree.GetBranch("wmass")
tau21Branch = myTree.GetBranch("tau21")

tagMassPass = 0
antitagMassPass = 0
tagTotalPass = 0
antitagTotalPass = 0

for event in myTree:
	wmass = event.wmass
	tau21 = event.tau21
	if (wmass > 65 and wmass < 95):
		tagMassPass+=1
		if (tau21 <0.4):
			tagTotalPass+=1
	else:
		antitagMassPass+=1
		if (tau21 <0.4):
			antitagTotalPass+=1

print "tagMassPass = " + str(tagMassPass)
print "tagTotalPass = " + str(tagTotalPass)
print "antitagMassPass = " + str(antitagMassPass)
print "antitagTotalPass = " + str(antitagTotalPass)