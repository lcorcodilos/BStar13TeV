import ROOT
from ROOT import *

import Bstar_Functions_local
from Bstar_Functions_local import LoadCuts

# tree is a tree
# var is the string fed to .Project
# histinfo is a list [string(title),int(bins),int(min),int(max)]
def ProjectScaledTreeVar(tree, var, cuts, histinfo):
	# Create a hist
	hist = TH1F(histinfo[0],histinfo[0],histinfo[1],histinfo[2],histinfo[3])

	tree.Project(histinfo[0], var, cuts)
	numberOfEntries = float(hist.Integral())
	print histinfo[0] + ' numberOfEntries = ' + str(numberOfEntries)

	hist.Scale(1/numberOfEntries)

	return hist

def LoadTCuts(cutset):
	# Load cuts
	cuts = LoadCuts(cutset)
	allCuts = {}
	# Grab each
	for var in cuts.keys():
		down = str(cuts[var][0])
		up = str(cuts[var][1])
		# Convert into a TCut
		if up != 'inf':
			allCuts[var] = TCut('(' + down + '<' + var + ') && (' + var + '<' + up + ')')
		else:
			allCuts[var] = TCut('(' + down + '<' + var + ')')

	return allCuts