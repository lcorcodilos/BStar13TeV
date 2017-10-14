import ROOT
from ROOT import *

from DataFormats.FWLite import Events, Handle

import Bstar_Functions_local
from Bstar_Functions_local import Load_Ntuples

files = Load_Ntuples('QCDHT700','')

jobs=5
num=1

jobiter = 0
splitfiles = []
for ifile in range(1,len(files)+1):
	if (ifile-1) % jobs == 0:
		jobiter+=1
	count_index = ifile  - (jobiter-1)*jobs
	if count_index==num:
		splitfiles.append(files[ifile-1])

events = Events(splitfiles)

print "Running over " +str(jobs)+ " jobs"
print "This will process job " +str(num)


GenHandle 	= 	Handle (  "vector<reco::GenParticle>")
GenLabel  	= 	( "filteredPrunedGenParticles" , "")

topsFound = 0
count = 0
for event in events:

	count	= 	count + 1

	if count % 10000 == 0 :
	  print  '--------- Processing Event ' + str(count)
	

	event.getByLabel ( GenLabel, GenHandle )
	GenParticles = GenHandle.product()

	for ig in GenParticles:
		# Find our top
		isT = ig.pdgId() == 6 and ig.status() == 22
		isTB = ig.pdgId() == -6 and ig.status() == 22
	
		if isT or isTB:
			topsFound+=1
			print '\rFound ' + str(topsFound) +' tops'

			print ig.daughterList()

			raw_input('waiting')



		# # if we have one...
		# if isT or isTB:
		# 	# Create a 3-vector
		# 	Tvect = TVector3()
		# 	Tvect.SetPtEtaPhi(ig.pt(),ig.eta(),ig.phi())

		# 	# Go through all genparticles again
		# 	for jg in GP:
		# 		# Check 