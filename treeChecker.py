import ROOT
from ROOT import *
import Bstar_Functions
from Bstar_Functions import *
import glob

# Need to create a dictionary of the different files with their different s


treeFiles = glob.glob('TTrees/*none.root')

for file in treeFiles:
	# search for name of set in string
	# Maybe remove 'TWtreefile_' and '_Trigger_nominal_none.root'

	# Search output files for the set string from above
	# This will be a list with all possible log files (signals and ttbar will have JER, JES, etc)

	# Search this list of output files for 'JER', 'JES', and 'Pileup'
	# If it DOESN'T have this, take it as the final file

	# Compare the line ''
