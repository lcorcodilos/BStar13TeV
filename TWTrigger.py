#! /usr/bin/env python

###################################################################
##								 ##
## Name: TWrate.py						 ##
## Author: Kevin Nash 						 ##
## Date: 5/28/2015						 ##
## Purpose: This program creates the numerator and denominator 	 ##
##          used by TWTrigger_Maker.py to create trigger  	 ##
##          Efficiency curves.					 ##
##								 ##
###################################################################

import os
import glob
import math
from math import sqrt,exp
import ROOT
from ROOT import std,ROOT,TFile,TLorentzVector,TMath,gROOT, TF1,TH1F,TH1D,TH2F,TH2D
from ROOT import TVector
from ROOT import TFormula

import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
from array import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'data',
				  dest		=	'set',
				  help		=	'dataset (ie data,ttbar etc)')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'ptreweight',
				  help		=	'on or off')

parser.add_option('-n', '--num', metavar='F', type='string', action='store',
				  default	=	'all',
				  dest		=	'num',
				  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default	=	'1',
				  dest		=	'jobs',
				  help		=	'number of jobs')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default	=	'file',
				  dest		=	'split',
				  help		=	'split by event of file')

parser.add_option('-b', '--bx', metavar='F', type='string', action='store',
				  default	=	'25ns',
				  dest		=	'bx',
				  help		=	'bunch crossing 50ns or 25ns')

parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				  default	=	'HLT_PFHT900,HLT_AK8PFJet450', #,'HLT_PFHT800_v2',#
				  dest		=	'tname',
				  help		=	'trigger name')

parser.add_option('-p', '--pretname', metavar='F', type='string', action='store',
				  default	=	'HLT_PFHT475_v3',#'NONE',
				  dest		=	'pretname',
				  help		=	'prescaled trigger name')


(options, args) = parser.parse_args()



#If running on the grid we access the script within a tarred directory
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')
gROOT.Macro(di+"rootlogon.C")
import Bstar_Functions	
from Bstar_Functions import *


tname = options.tname.split(',')
tnamestr = ''
Tstr = [options.pretname]
for iname in range(0,len(tname)):
	tnamestr+=tname[iname]
	if iname!=len(tname)-1:
		tnamestr+='OR'
	Tstr.append(tname[iname])

print Tstr

#Load up cut values based on what selection we want to run 
Cuts = LoadCuts("default")
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
sjbtag = Cuts['sjbtag']
tau32 = Cuts['tau32']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']




print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""



#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"


#Based on what set we want to analyze, we find all Ntuple root files 
files = Load_Ntuples(options.set,di)
jobiter = 0
# We select all the events: 
splitfiles = []


#For event counting
jobiter = 0
splitfiles = []

if jobs != 1 and options.split=="file":
	for ifile in range(1,len(files)+1):
		if (ifile-1) % jobs == 0:
			jobiter+=1
		count_index = ifile  - (jobiter-1)*jobs
		if count_index==num:
			splitfiles.append(files[ifile-1])

	events = Events(splitfiles)
	runs = Runs(splitfiles)

if options.split=="event" or jobs == 1:	  
	events = Events(files)
	runs = Runs(files)

nevHandle 	= 	Handle (  "vector<int> "  )
nevLabel  	= 	( "counter" , "nevr")

totnev = 0
for run in runs:
		run.getByLabel (nevLabel,nevHandle )
		nev 		= 	nevHandle.product() 
		totnev+=nev[0]
print "Total unfiltered events in selection: ",totnev


# if jobs != 1 and options.split=="file":
# 	for ifile in range(1,len(files)+1):
# 		if (ifile-1) % jobs == 0:
# 			jobiter+=1
# 	count_index = ifile  - (jobiter-1)*jobs
# 	if count_index==num:
# 		splitfiles.append(files[ifile-1])

# 	events = Events (splitfiles)
# if options.split=="event" or jobs == 1:	  
# 	events = Events (files)
#events = ChainEvent(files)
#Here we load up handles and labels.
#These are used to grab entries from the Ntuples.
#To see all the current types in an Ntuple use edmDumpEventContent /PathtoNtuple/Ntuple.root

AK8HL = Initlv("jetsAK8")

GeneratorHandle 	= 	Handle (  "GenEventInfoProduct")
GeneratorLabel  	= 	( "generator" , "")

puHandle    	= 	Handle("int")
puLabel     	= 	( "eventUserData", "puNtrueInt" )

softDropPuppiMassHandle		=	Handle (  "vector<float> "  )
softDropPuppiMassLabel		=	( "jetsAK8" , "jetAK8PuppiCorrectedsoftDropMass")

vsubjets0indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets0indexLabel  	= 	( "jetsAK8" , "jetAK8PuppivSubjetIndex0")

vsubjets1indexHandle 	= 	Handle (  "vector<float> "  )
vsubjets1indexLabel  	= 	( "jetsAK8" , "jetAK8PuppivSubjetIndex1")

subjetsAK8CSVHandle 	= 	Handle (  "vector<float> "  )
subjetsAK8CSVLabel  	= 	( "subjetsAK8Puppi" , "subjetAK8PuppiCSVv2")

tau1Handle 	= 	Handle (  "vector<float> "  )
tau1Label  	= 	( "jetsAK8" , "jetAK8Puppitau1")

tau2Handle 	= 	Handle (  "vector<float> "  )
tau2Label  	= 	( "jetsAK8" , "jetAK8Puppitau2")

tau3Handle 	= 	Handle (  "vector<float> "  )
tau3Label  	= 	( "jetsAK8" , "jetAK8Puppitau3")

HT475Handle	=	Handle ( "vector<bool>" )
HT475Label	=	( "Filter" , "HT475bit" )

HT800Handle	=	Handle ( "vector<bool>" )
HT800Label	=	( "Filter" , "HT800bit" )

HT900Handle = Handle ( "vector<bool>" )
HT900Label = ("Filter", "HT900bit")

JET450Handle	=	Handle ( "vector<bool>" )
JET450Label = ("Filter","JET450bit")



#---------------------------------------------------------------------------------------------------------------------#

#Create the output file
if jobs != 1:
	f = TFile( "TWTrigger"+options.set+tnamestr+"_pre_"+options.pretname+"_job"+options.num+"of"+options.jobs+".root", "recreate" )
else:
	f = TFile( "triggerstudies/TWTrigger"+options.set+tnamestr+"_pre_"+options.pretname+".root", "recreate" )




print "Creating histograms"

#Define Histograms
f.cd()
nev = TH1F("nev",	"nev",		1, 0, 1 )
nev.SetBinContent(1,totnev)
#---------------------------------------------------------------------------------------------------------------------#
Htpreuntrig          = TH1D("Htpreuntrig",           "",             400,  0,  4000 )
Htuntrig          = TH1D("Htuntrig",           "",             400,  0,  4000 )

Htpreuntrig.Sumw2()
Htuntrig.Sumw2()


Htpre          = TH1D("Htpre",           "",             400,  0,  4000 )
Ht          = TH1D("Ht",           "",             400,  0,  4000 )

Htpre.Sumw2()
Ht.Sumw2()

Htprettags          = TH1D("Htprettags",           "",             400,  0,  4000 )
Htttags         = TH1D("Htttags",           "",             400,  0,  4000 )

Htprettags.Sumw2()
Htttags.Sumw2()


Ptpre          = TH1D("Ptpre",           "",             200,  0,  2000 )
Pt          = TH1D("Pt",           "",             200,  0,  2000 )


Ptpre.Sumw2()
Pt.Sumw2()

Mpre          = TH1D("Mpre",           "",             100,  0,  200 )
M          = TH1D("M",           "",             100,  0,  200 )


Mpre.Sumw2()
M.Sumw2()


#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0

print "Start looping"
#initialize the ttree variables
totevents = events.size()
print str(totevents)  +  ' Events total'

# Setup some pre-loop variables
trigdict = {} # Filled with the trigger names as keys and trigger bits as values
prestrig = options.pretname # defaults to NONE and nothing happens
noPassCount = 0

for event in events:

	count	= 	count + 1

	if count % 100000 == 0 :
		print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '


	# Grab bits for event
	event.getByLabel(HT475Label, HT475Handle)
	HT475bit = HT475Handle.product()
	event.getByLabel(HT800Label, HT800Handle)
	HT800bit = HT800Handle.product()
	event.getByLabel (HT900Label, HT900Handle)
	HT900bit = HT900Handle.product()
	event.getByLabel (JET450Label, JET450Handle)
	JET450bit = JET450Handle.product()

	# Store bits in list
	trigdict['HLT_PFHT475_v3'] = HT475bit
	trigdict['HLT_PFHT800_v2'] = HT800bit
	trigdict['HLT_PFHT900'] = HT900bit
	trigdict['HLT_AK8PFJet450'] = JET450bit


	AK8LV = Makelv(AK8HL,event)

	if len(AK8LV)==0:
		continue

	tindex,windex = Hemispherize(AK8LV,AK8LV)

	# if jobs != 1 and options.split=="event":
	# 	if (count - 1) % jobs == 0:
	# 		jobiter+=1
	# 	count_index = count - (jobiter-1)*jobs
	# 	if count_index!=num:
	# 		continue 
	
	wJetsh1 = []
	wJetsh0  =  []
	topJetsh1 = []
	topJetsh0  = []

	for i in range(0,len(windex[1])):
		wJetsh1.append(AK8LV[windex[1][i]])
	for i in range(0,len(windex[0])):
		wJetsh0.append(AK8LV[windex[0][i]])
	for i in range(0,len(tindex[1])):
		topJetsh1.append(AK8LV[tindex[1][i]])
	for i in range(0,len(tindex[0])):
		topJetsh0.append(AK8LV[tindex[0][i]])
	
	wjh0 = 0
	wjh1 = 0

	#Require 1 pt>150 jet in each hemisphere (top jets already have the 150GeV requirement) 

	for wjet in wJetsh0:
		if wjet.Perp() > 400.0:
			wjh0+=1
	for wjet in wJetsh1:
		if wjet.Perp() > 400.0:
			wjh1+=1
	njets11w0 	= 	((len(topJetsh1) == 1) and (wjh0 == 1))
	njets11w1 	= 	((len(topJetsh0) == 1) and (wjh1 == 1))
	#We consider both the case that the b is the leading (highest pt) jet (hemis0) and the case where the top is the leading jet (hemis1)
	for hemis in ['hemis0']:#,'hemis1']:
		if hemis == 'hemis0'   :
			if not njets11w0:
				continue 
			#The Ntuple entries are ordered in pt, so [0] is the highest pt entry
			#We are calling a candidate b jet (highest pt jet in hemisphere0)  

			tindexval = tindex[1][0]
			windexval = windex[0][0]

			wjet = wJetsh0[0]
			tjet = topJetsh1[0]

		if hemis == 'hemis1'  :
			if not njets11w1:
				continue 

			tindexval = tindex[0][0]
			windexval = windex[1][0]

			wjet = wJetsh1[0]
			tjet = topJetsh0[0]
		
		HT = tjet.Perp() + wjet.Perp()
		PT = tjet.Perp()

		event.getByLabel (softDropPuppiMassLabel, softDropPuppiMassHandle)
		puppiJetMass 	= 	softDropPuppiMassHandle.product()

		MA = puppiJetMass[tindexval]

		tmass_cut = tmass[0]<puppiJetMass[tindexval]<tmass[1]
		wmass_cut = wmass[0]<=puppiJetMass[windexval]<wmass[1]

		#event.getByLabel (TpsLabel, TpsHandle)
		#Tps 		= 	TpsHandle.product() 

		TRIGBOOL = []
		presTRIGBOOL = False
		

		for t in trigdict.keys():
			# If the trigger is the prescale trigger, save a trigger bit other than FALSE
			if t==prestrig:
				presTRIGBOOL = trigdict[t]
				# print "-----FOUND-----"
				# print "prescale " + str(t)
				# print "-----FOUND-----"
			# Add it to the list of trigger booleans
			elif t in Tstr:
				TRIGBOOL.append(trigdict[t])
		

		# If there's no prescale trigger, make the bool true
		if options.pretname == 'NONE':
			presTRIGBOOL = True

		# Initialize...
		TPASS = False

		# If the event passes any of the triggers, pass the event and stop checking if it passes others (break for loop)
		for TB in TRIGBOOL:
			if TB:
				#TPASS = True
				break
			else:
				print "trigger failed"
				raw_input('continue') 	


		# Fill HT histo for all events
		Htpreuntrig.Fill(HT)
		if TPASS:
			# and another for events that pass one trigger
			Htuntrig.Fill(HT)

		# If we don't pass the prescale trigger, go on to the next event
		if not presTRIGBOOL:
			continue 

		# Fill HT, Pt, and Mass distributions, pre pass but DO pass prescale
		Htpre.Fill(HT)
		Ptpre.Fill(PT)
		Mpre.Fill(MA)


		# Fill HT, Pt, and Mass distributions, post pass but DO pass prescale
		if TPASS:
			Ht.Fill(HT)
			Pt.Fill(PT)
			M.Fill(MA)

		event.getByLabel (vsubjets0indexLabel,vsubjets0indexHandle )
		vsubjets0index 		= 	vsubjets0indexHandle.product() 

		event.getByLabel (vsubjets1indexLabel,vsubjets1indexHandle )
		vsubjets1index 		= 	vsubjets1indexHandle.product() 

		event.getByLabel (subjetsAK8CSVLabel,subjetsAK8CSVHandle )
		subjetsAK8CSV		= 	subjetsAK8CSVHandle.product() 


		if len(subjetsAK8CSV)==0:
			continue
		if len(subjetsAK8CSV)<2:
			subjetsAK8CSV[int(vsubjets0index[tindexval])]
		else:
			SJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[tindexval])],subjetsAK8CSV[int(vsubjets1index[tindexval])]]

		SJ_csvmax = max(SJ_csvvals)
		sjbtag_cut = sjbtag[0]<SJ_csvmax<=sjbtag[1]

		# If we pass top tagging
		if sjbtag_cut and tmass_cut: 
			Htprettags.Fill(HT)
			if TPASS:
				Htttags.Fill(HT)

f.cd()
f.Write()
f.Close()
# for key in trigdict.keys():
# 	print key
# 	print trigdict[key]
# 	print str(trigdict[key]/count)+'%'
# 	print 

print "Trigger failed: " + str(noPassCount)
print "number of events: " + str(count)
