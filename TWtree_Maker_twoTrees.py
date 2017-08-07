#! /usr/bin/env python



###################################################################
##								 ##
## Name: TWrate.py						 ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program creates eta binned tags and probes 	 ##
##          as a function of Pt for data and MC for use with 	 ##
##          TWrate_Maker.py.					 ##
##								 ##
###################################################################

import os
import glob
import math
from math import sqrt,exp
import ROOT
from ROOT import std,ROOT,TFile,TLorentzVector,TMath,gROOT, TF1,TH1F,TH1D,TH2F,TH2D,TTree
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
parser.add_option('-J', '--JES', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JES',
				  help		=	'nominal, up, or down')
parser.add_option('-R', '--JER', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'JER',
				  help		=	'nominal, up, or down')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				   default	=	'HLT_PFHT900,HLT_AK8PFJet450',
				   dest		=	'tname',
				   help		=	'trigger name')
parser.add_option('-y', '--modmass', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'modmass',
				  help		=	'nominal up or down')
parser.add_option('-p', '--pdfweights', metavar='F', type='string', action='store',
				  default	=	'nominal',
				  dest		=	'pdfweights',
				  help		=	'nominal, up, or down')
parser.add_option('-x', '--pileup', metavar='F', type='string', action='store',
				  default	=	'on',
				  dest		=	'pileup',
				  help		=	'If not data do pileup reweighting?')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-m', '--modulesuffix', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'modulesuffix',
				  help		=	'ex. PtSmearUp')
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
                  default	=	'all',
                  dest		=	'num',
                  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
                  default	=	'1',
                  dest		=	'jobs',
                  help		=	'number of jobs')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
                  default	=	'file',
                  dest		=	'split',
                  help		=	'split by event of file') #EVENT SPLITTING DOESN'T CURRENTLY WORK

(options, args) = parser.parse_args()

#------------------Jet energy mods--------------------------------
# Helps grab the propper AK8 jet information
mod = ''
post = ''
if options.JES!='nominal':
	mod = mod + 'JES_' + options.JES
	post='jes'+options.JES
if options.JER!='nominal':
	mod = mod + 'JER_' + options.JER
	post='jer'+options.JER

#--------------------- Trigger------------------------------------
# We check that the data passes the trigger
tname = options.tname.split(',')
tnamestr = ''
for iname in range(0,len(tname)):
	tnamestr+=tname[iname]
	if iname!=len(tname)-1:
		tnamestr+='OR'
		
trig='none'
if options.set!= 'data' and options.tname!='none': 
	if options.tname=='HLT_PFHT900,HLT_AK8PFJet450':
		trig = 'nominal'
	elif options.tname!= []:
		trig = 'tnamestr'
		
if tnamestr=='HLT_PFHT900ORHLT_AK8PFJet450':
	tnameformat='nominal'
elif tnamestr=='':
	tnameformat='none'
else:
	tnameformat=tnamestr
#--------------------- PDFs-----------------------------------------
# Currently commented out since we don't use it
pstr = ""
# if options.pdfweights!="nominal":
# 	print "using pdf uncertainty"
# 	pstr = "_pdf_"+options.pdfset+"_"+options.pdfweights

#---------------------Pileup----------------------------------------
# Need to grab a pileBin for each hemi
pustr = ""
if options.pileup=='off':
	pustr = "pileup_unweighted"
if options.pileup=='up':
	pustr = "pileup_up"
if options.pileup=='down':
	pustr = "pileup_down"
mod = mod+pustr
if mod == '':
	mod = options.modulesuffix

print "mod = " + mod

#---------------------Mod mass----------------------------------------
# Not used because a mod mass plot hasn't been made yet!
# mmstr = ""
# if options.modmass!="nominal":
# 	print "using modm uncertainty"
# 	mmstr = "_modm_"+options.modmass
#------------------------------------------------------------------------
#If running on the grid we access the script within a tarred directory
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")
import Bstar_Functions	
from Bstar_Functions import *

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

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :
	settype = options.set

print 'The type of set is ' + settype

# We select all the events:    
events = Events (files)

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


#Here we load up handles and labels.
#These are used to grab entries from the Ntuples.
#To see all the current types in an Ntuple use edmDumpEventContent /PathtoNtuple/Ntuple.root

AK8HL = Initlv("jetsAK8",post)
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

# HT800Handle	=	Handle ( "vector<bool>" )
# HT800Label	=	( "Filter" , "HT800bit" )

HT900Handle = Handle ( "vector<bool>" )
HT900Label = ("Filter", "HT900bit")

JET450Handle	=	Handle ( "vector<bool>" )
JET450Label = ("Filter","JET450bit")


#---------------------------------------------------------------------------------------------------------------------#

#Create the output file
if jobs != 1:
	f = TFile( "TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+"_job"+options.num+"of"+options.jobs+".root", "recreate" )
else:
	f = TFile( "TWtreefile_"+options.set+"_Trigger_"+tnameformat+"_"+mod+pstr+".root", "recreate" )


f.cd()
nev = TH1F("nev",	"nev",		1, 0, 1 )
nev.SetBinContent(1,totnev)


#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
passedNev = 0
print "Start looping"
#initialize the ttree variables
#Only store nev in regular tree now
# Commented out since it's stored in a histo
# tree_vars = {"nev":array('d',[totnev])}#,"nsubjets":array('d',[0.])
# Tree = Make_Trees(tree_vars)
# Tree.Fill()

#totevents = events.size()
#print "Total events in edmntuple form: " + str(totevents)

# This tree is done now

# Now book a tree for each of the jets (leading and subleading) 
# These jets can be identified based on hemisphere. Hemi0 has the leading jet
leading_vars = {
	"SDmass":array('d',[0]),
	"tau1":array('d',[0]),
	"tau2":array('d',[0]),
	"tau3":array('d',[0]),
	"sjbtag":array('d',[0]),
	"pt":array('d',[0]),
	"eta":array('d',[0]),
	"phi":array('d',[0]),
	"mass":array('d',[0])}

subleading_vars = {
	"SDmass":array('d',[0]),
	"tau1":array('d',[0]),
	"tau2":array('d',[0]),
	"tau3":array('d',[0]),
	"sjbtag":array('d',[0]),
	"pt":array('d',[0]),
	"eta":array('d',[0]),
	"phi":array('d',[0]),
	"mass":array('d',[0])}

leadingTree = TTree("leadingTree", "leadingTree")
for v in leading_vars.keys():
	leadingTree.Branch(v, leading_vars[v], v+"/D")
leadingTree.AutoSave("Overwrite")


subleadingTree = TTree("subleadingTree", "subleadingTree")
for v in subleading_vars.keys():
	subleadingTree.Branch(v, subleading_vars[v], v+"/D")
subleadingTree.AutoSave("Overwrite")


if options.set != 'data':
	leading_vars['pileBin'] = array('i',[0])
	subleading_vars['pileBin'] = array('i',[0])
	leadingTree.Branch('pileBin',leading_vars['pileBin'],'pileBin/I')
	subleadingTree.Branch('pileBin',subleading_vars['pileBin'],'pileBin/I')


# Now we can loop
# We check for the trigger on data, do pt cuts on the jets, and eta cuts
for event in events:
	count	= 	count + 1

	if count % 100000 == 0 :
	  print  '--------- Processing Event ' + str(count) #+'   -- percent complete ' + str(100*count/totevents) + '% -- '
	
	# Need to ask Kevin about the indices here
	if options.set == 'data':
		event.getByLabel (HT900Label, HT900Handle)
		HT900bit = HT900Handle.product()
		event.getByLabel (JET450Label, JET450Handle)
		JET450bit = JET450Handle.product()

		try:
			trigbits = [JET450bit[0],HT900bit[0]]
		except:
			trigbits = [HT900bit[0]]

		passt = False
		for t in trigbits:
			if t:
				passt = True
		if not passt:
			continue

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
		if ht < 1100.0:
			continue


		if abs(leadingJet.Eta())<2.40 and abs(subleadingJet.Eta())<2.40:
			# Grab ntuple value vectors
			event.getByLabel (softDropPuppiMassLabel, softDropPuppiMassHandle)
			puppiJetMass 	= 	softDropPuppiMassHandle.product()

			event.getByLabel (tau3Label, tau3Handle)
			Tau3		= 	tau3Handle.product() 

			event.getByLabel (tau2Label, tau2Handle)
			Tau2		= 	tau2Handle.product() 

			event.getByLabel (tau1Label, tau1Handle)
			Tau1		= 	tau1Handle.product() 

			event.getByLabel (vsubjets0indexLabel,vsubjets0indexHandle )
			vsubjets0index 		= 	vsubjets0indexHandle.product() 

			event.getByLabel (vsubjets1indexLabel,vsubjets1indexHandle )
			vsubjets1index 		= 	vsubjets1indexHandle.product() 

			event.getByLabel (subjetsAK8CSVLabel,subjetsAK8CSVHandle )
			subjetsAK8CSV		= 	subjetsAK8CSVHandle.product() 


			if len(subjetsAK8CSV)==0:
				continue
			if len(subjetsAK8CSV)<2:
				leadSJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[leadingIndexVal])]]
				subSJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[subleadingIndexVal])]]
			else:
				leadSJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[leadingIndexVal])],subjetsAK8CSV[int(vsubjets1index[leadingIndexVal])]]
				subSJ_csvvals = [subjetsAK8CSV[int(vsubjets0index[subleadingIndexVal])],subjetsAK8CSV[int(vsubjets1index[subleadingIndexVal])]]


			if leadSJ_csvvals != [] and subSJ_csvvals != []: #added this because files with no SJ_csvvals would cause the entire thing to fail			
				leadSJ_csvmax = max(leadSJ_csvvals)
				subSJ_csvmax = max(subSJ_csvvals)

				leadingTemp_vars = {
					"SDmass":puppiJetMass[leadingIndexVal],
					"tau1":Tau1[leadingIndexVal],
					"tau2":Tau2[leadingIndexVal],
					"tau3":Tau3[leadingIndexVal],		
					"sjbtag":leadSJ_csvmax,
					"pt":leadingJet.Perp(),
					"eta":leadingJet.Eta(),
					"phi":leadingJet.Phi(),
					"mass":leadingJet.M()}

				subleadingTemp_vars = {
					"SDmass":puppiJetMass[subleadingIndexVal],
					"tau1":Tau1[subleadingIndexVal],
					"tau2":Tau2[subleadingIndexVal],
					"tau3":Tau3[subleadingIndexVal],		
					"sjbtag":subSJ_csvmax,
					"pt":subleadingJet.Perp(),
					"eta":subleadingJet.Eta(),
					"phi":subleadingJet.Phi(),
					"mass":subleadingJet.M()}


				# Get pileup info if not data
				if options.set != 'data':
					PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
					if options.pileup=='up':
						PilePlot = PileFile.Get("Pileup_Ratio_up")
					elif options.pileup=='down':
						PilePlot = PileFile.Get("Pileup_Ratio_down")
					else:	
						PilePlot = PileFile.Get("Pileup_Ratio")

					event.getByLabel (puLabel, puHandle)
					PileUp 		= 	puHandle.product()
					leadingTemp_vars['pileBin'] = PilePlot.FindBin(PileUp[0])
					subleadingTemp_vars['pileBin'] = PilePlot.FindBin(PileUp[0])

				passedNev += 1

				for key in leading_vars.keys():
					leading_vars[key][0] = leadingTemp_vars[key]
				try:
					leadingTree.Fill()
				except:
					print "Failure at " + str(count)

				for key in subleading_vars.keys():
					subleading_vars[key][0] = subleadingTemp_vars[key]
				subleadingTree.Fill()

				# for key in leading_vars.keys():
				# 	print str(key) + ": " + str(leading_vars[key][0])
				# leadingTree.Fill()
				# raw_input("continue...")
print "Events in edmntuple: " + str(count)
print "Events that passed: " + str(passedNev)

f.cd()
f.Write()
f.Close()