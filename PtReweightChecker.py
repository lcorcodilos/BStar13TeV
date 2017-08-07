import ROOT
from ROOT import *

from DataFormats.FWLite import Events, Handle

from math import sqrt, exp

import Bstar_Functions
from Bstar_Functions import *

files = Load_Ntuples('ttbarscaleup','')
events = Events(files)

GenHandle 	= 	Handle (  "vector<reco::GenParticle>")
GenLabel  	= 	( "filteredPrunedGenParticles" , "")

isTcount = 0
isTBcount = 0
LowPtCount = 0
nothingChanged = 0
# idIsSix = 0
# idIsNsix = 0
# statusCount = 0

# isTop = 0
# isAntiTop = 0
passed = 0

# top22highpt = 0
# top22lowpt = 0
# top62highpt = 0
# top62lowpt = 0

# antitop22highpt = 0
# antitop22lowpt = 0
# antitop62highpt = 0
# antitop62lowpt = 0

# statusValsTop1 = {}
# statusValsAntiTop1 = {}
# statusValsTop2 = {}
# statusValsAntiTop2 = {}

AK8HL = Initlv("jetsAK8",'')

for event in events:

	AK8LV = Makelv(AK8HL,event)

	if len(AK8LV)==0:
		continue

	# Only need one of these since they are identical
	tindex,windex = Hemispherize(AK8LV,AK8LV)
	index = tindex

	Jetsh1=[]
	Jetsh0=[]
	
	for i in range(0,len(index[1])):
		Jetsh1.append(AK8LV[index[1][i]])
	for i in range(0,len(index[0])):
		Jetsh0.append(AK8LV[index[0][i]])
	
	jh0 = 0
	jh1 = 0
	
	#Require 1 pt>400 jet in each hemisphere
	for jet in Jetsh0:
		if jet.Perp() > 400.0:
			jh0+=1
	for jet in Jetsh1:
		if jet.Perp() > 400.0:
			jh1+=1

	njetsBit 	= 	((jh1 >= 1) and (jh0 >= 1))


	if njetsBit:
		leadingJet = Jetsh0[0]
		subleadingJet = Jetsh1[0]

		leadingIndexVal = index[0][0]
		subleadingIndexVal = index[1][0]

		# MANUAL HT CUT -- TAKE OUT WHEN TRIGGER CORRECTION FINALIZED
		ht = leadingJet.Perp() + subleadingJet.Perp()
		# if ht < 1100.0:
		# 	continue


		if abs(leadingJet.Eta())<2.40 and abs(subleadingJet.Eta())<2.40:
			passed += 1
			# For pt reweighting
			event.getByLabel ( GenLabel, GenHandle )
			GenParticles = GenHandle.product()
			
			genTpt = -100.
			genTBpt = -100	
			for ig in GenParticles:
				isT = ig.pdgId() == 6 and ig.status() == 22
				isTB = ig.pdgId() == -6 and ig.status() == 22

				# if ig.pdgId() == 6:
				# 	idIsSix += 1
				# elif ig.pdgId() == -6:
				# 	idIsNsix += 1

				# stat = ig.status()
				# daughter1 = ig.daughter1()
				# daughter2 = ig.daughter2()

				# if ig.pdgId() == 6:
				# 	isTop += 1

				# 	if str(stat) in statusValsTop1:
				# 		statusValsTop1[str(daughter1)] += 1
				# 	else:
				# 		statusValsTop1[str(daughter1)] = 1

				# 	if str(stat) in statusValsTop2:
				# 		statusValsTop2[str(daughter2)] += 1
				# 	else:
				# 		statusValsTop2[str(daughter2)] = 1
					
				# 	# PT stuff
				# 	if stat == 22:
				# 		if ig.p() > 400:
				# 			top22highpt += 1
				# 		else:
				# 			top22lowpt += 1
				# 	elif stat == 62:
				# 		if ig.p() > 400:
				# 			top62highpt += 1
				# 		else:
				# 			top62lowpt += 1

				# if ig.pdgId() == -6:
				# 	isAntiTop += 1

				# 	if str(stat) in statusValsAntiTop1:
				# 		statusValsAntiTop1[str(daughter1)] += 1
				# 	else:
				# 		statusValsAntiTop1[str(daughter1)] = 1

				# 	if str(stat) in statusValsAntiTop2:
				# 		statusValsAntiTop2[str(daughter2)] += 1
				# 	else:
				# 		statusValsAntiTop2[str(daughter2)] = 1
					
				# 	# PT stuff 
				# 	if stat == 22:
				# 		if ig.p() > 400:
				# 			antitop22highpt += 1
				# 		else:
				# 			antitop22lowpt += 1
				# 	elif stat == 62:
				# 		if ig.p() > 400:
				# 			antitop62highpt += 1
				# 		else:
				# 			antitop62lowpt += 1


				if isT:
					genTpt = ig.pt()
					isTcount += 1
				if isTB:
					genTBpt = ig.pt()
					isTBcount += 1	

			if (genTpt<0) or (genTBpt<0):
				LowPtCount += 1
			if genTpt == -100 and genTBpt == -100:
				nothingChanged += 1
			wTPt = exp(0.156-0.00137*genTpt)
			wTbarPt = exp(0.156-0.00137*genTBpt)

print "is T: " + str(isTcount)
print "is TB: " + str(isTBcount)
print "Low pt: " + str(LowPtCount)
print "Nothing changed: " + str(nothingChanged)
# print "ID is 6: " + str(idIsSix)
# print "ID is -6: " + str(idIsNsix)
# print "Status is 3: " + str(statusCount)

# print "Passed events: " + str(passed)
# print "Is Top: " + str(isTop)
# print "is Anti Top: " + str(isAntiTop)

# print "top22highpt: " + str(top22highpt)
# print "top22lowpt: " + str(top22lowpt)
# print "top62highpt: " + str(top62highpt)
# print "top62lowpt: " + str(top62lowpt)

# print "antitop22highpt" + str(antitop22highpt)
# print "antitop22lowpt" + str(antitop22lowpt)
# print "antitop62highpt" + str(antitop62highpt)
# print "antitop62lowpt" + str(antitop62lowpt)

# print "Top daughter 1 Vals"
# print "--------------------"
# for i in statusValsTop1:
# 	print i + ": " + str(statusValsTop1[i])
# print '\n'

# print "Top daughter 2 Vals"
# print "--------------------"
# for i in statusValsTop2:
# 	print i + ": " + str(statusValsTop2[i])
# print '\n'

# print "Anti Top daughter 1 Vals"
# print "--------------------"
# for i in statusValsAntiTop1:
# 	print i + ": " + str(statusValsAntiTop1[i])
# print '\n'

# print "Anti Top daughter 2 Vals"
# print "--------------------"
# for i in statusValsAntiTop2:
# 	print i + ": " + str(statusValsAntiTop2[i])
# print '\n'
