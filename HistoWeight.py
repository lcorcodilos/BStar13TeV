import os
import array
import glob
import math
import ROOT
import sys
from ROOT import *
from array import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-i', '--inputf', metavar='F', type='string', action='store',
                  default	=	'NULL_INPUT',
                  dest		=	'inputf',
                  help		=	'input root file')

parser.add_option('-w', '--weight', metavar='F', type='float', action='store',
                  default=1.0,
                  dest='weight',
                  help='weight')

parser.add_option('-n', '--nev', metavar='F', type='string', action='store',
                  default	=	'default',
                  dest		=	'nev',
                  help		=	'default or auto')

parser.add_option('-o', '--outputf', metavar='F', type='string', action='store',
                  default	=	'NULL_OUTPUT',
                  dest		=	'outputf',
                  help		=	'output root file')

(options, args) = parser.parse_args()

# Import file
infile = ROOT.TFile(options.inputf)
# Create an output file
output = ROOT.TFile(options.outputf, "recreate")

#Call the list of items in the input file (nev histo and Tree)
D = infile.GetListOfKeys()


weight = options.weight
evweight=1.0
if options.nev=='auto':
	# Read in the number of events of the file 
	events = infile.Get('nev')
	# Create a weight to scale for number of events
	evweight = 1.0/float(events.Integral())
	print "Number of Events: ",events.Integral()
Good=True

# Multiply original weight by the new # of event weight
weight*=evweight


try :
	# Initialize array 'reweight' with one entry of zero
	reweight = array('d',[0.])
	# Create the weight tree in input file
	weighttree = infile.Get('Weight')
	# Create the branch in weighttree for the array
	weighttree.SetBranchAddress("weightv",reweight)
	# Gets "weightv"
	weighttree.GetEntry(0)
	print "reweighting. Previous weight " +  str(reweight[0])


except :
	# Initialize reweight with one entry of one
	reweight =array('d',[1.])

# Check if the file is empty
if len(D)==0:
	Good = False

# Loop through items of input file
for i in range(0,len(D)):
	# Grab the actual tree/histo/etc
	a = D[i].ReadObj()
	try:
		# Scale the object by weight/reweight
		a.Scale(weight/reweight[0])
		a.Write()
		#print "scaled " + str(a.GetName())
	except:
		if  a.GetName() != 'Weight':
			# if the object is not the weight tree 
			print "not scaling " + str(a.GetName()) 
			a.CloneTree().Write()

# If the file is NOT empty
if Good:
	# Initialize a new array and ttree
	weightv = array('d',[weight])
	t = TTree("Weight", "Weight");
	# Initialize a branch in the new tree and fill it
	t.Branch('weightv',weightv, "weightv/D")
	#weightv = weight
	t.Fill()
	t.Write()
	output.Close()

else:
	raise Exception('BAD ROOT FILE!')
	output.Close()

