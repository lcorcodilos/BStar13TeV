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
from ROOT import std,ROOT,TFile,TLorentzVector,TMath,gROOT, TF1,TH1F,TH1D,TH2F,TH2D, TH1I
from ROOT import TVector
from ROOT import TFormula

import sys
#from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
from array import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
				  default	=	'data',
				  dest		=	'set',
				  help		=	'dataset (ie data,ttbar etc)')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
				  default	=	'off',
				  dest		=	'grid',
				  help		=	'running on grid off or on')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
				  default	=	'rate_default',
				  dest		=	'cuts',
				  help		=	'Cuts type (ie default, rate, etc)')
parser.add_option('-t', '--tname', metavar='F', type='string', action='store',
				   default	=	'HLT_PFHT900,HLT_PFHT800,HLT_JET450',
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
				  default	=	'off',
				  dest		=	'pileup',
				  help		=	'If not data do pileup reweighting?')
parser.add_option('-S', '--split', metavar='F', type='string', action='store',
				  default   =   'event',
				  dest      =   'split',
				  help      =   'split by event of file') #File splitting not used with ttrees!
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
				  default   =   'all',
				  dest      =   'num',
				  help      =   'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
				  default   =   '1',
				  dest      =   'jobs',
				  help      =   'number of jobs')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
				  default	=	'none',
				  dest		=	'ptreweight',
				  help		=	'on or off')

(options, args) = parser.parse_args()


print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""

tname = options.tname.split(',')
tnamestr = ''
for iname in range(0,len(tname)):
	tnamestr+=tname[iname]
	if iname!=len(tname)-1:
		tnamestr+='OR'

		
if tnamestr=='HLT_PFHT900ORHLT_PFHT800ORHLT_AK8PFJet450':
	tnameformat='nominal'
elif tnamestr=='':
	tnameformat='none'
else:
	tnameformat=tnamestr

#If running on the grid we access the script within a tarred directory
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")
import Bstar_Functions	
from Bstar_Functions import *

#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"


#Load up cut values based on what selection we want to run 
Cons = LoadConstants()
lumi = Cons['lumi']
Lumi = str(lumi/1000)+"fb"

Cuts = LoadCuts(options.cuts)
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']

#Based on what set we want to analyze, we find all Ntuple root files -----------------
#Since this is the rate script, don't care about mod and pstr so hard-coded off
mainDir = "/uscms_data/d3/lcorcodi/BStar13TeV/CMSSW_7_4_1/src/BStar13TeV/TTrees/"

file = TFile(mainDir + "TWtreefile_"+options.set+"_Trigger_nominal_none.root")

tree = file.Get("Tree")

if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='ttbar'
	run_b_SF = False
else :	
	settype = options.set

print 'The type of set is ' + settype

#--------------------------------------------------------------------------------------

if options.set != 'data':
	#Load up scale factors (to be used for MC only)
	TrigFile = TFile(di+"Triggerweight_2jethack_data.root")
	TrigPlot = TrigFile.Get("TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475")

	print "TriggerWeight_"+tnamestr+"_pre_HLT_PFHT475"
	
	PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	if options.pileup=='up':
		PilePlot = PileFile.Get("Pileup_Ratio_up")
	elif options.pileup=='down':
		PilePlot = PileFile.Get("Pileup_Ratio_down")
	else:   
		PilePlot = PileFile.Get("Pileup_Ratio")

nevHisto = file.Get("nev")
B2Gnev = nevHisto.Integral()/jobs

if jobs!=1:
	f = TFile( "TWratefile"+options.set+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+".root", "recreate" )
else:
	f = TFile( "TWratefile"+options.set+"_PSET_"+options.cuts+".root", "recreate" )

print "Creating histograms"

#Define Histograms
f.cd()
#---------------------------------------------------------------------------------------------------------------------#
hEta1Count = TH1I("eta1Count", "number of events in low eta region", 1, 0, 1)
hEta2Count = TH1I("eta2Count", "number of events in high eta region", 1, 0, 1)

pteta1pretag          = TH1D("pteta1pretag",           "t Probe pt in 0<Eta<0.8",             400,  0,  2000 )
pteta2pretag          = TH1D("pteta2pretag",           "t Probe pt in 0.8<Eta<2.4",             400,  0,  2000 )

pteta1          = TH1D("pteta1",           "t pt in 0<Eta<0.8",             400,  0,  2000 )
pteta2          = TH1D("pteta2",           "t pt in 0.8<Eta<2.4",             400,  0,  2000 )

Mpre          = TH1D("Mpre",           "top mass",             400,  105,  210 )
Mpre.Sumw2()

MpostFull          = TH1D("MpostFull",           "top mass in 0<Eta<2.4",             400,  105,  210 )
MpostFull.Sumw2()

MfailEta1 = TH1D("MfailEta1",           "top mass in 0<Eta<0.8",             400,  105,  210 )
MfailEta1.Sumw2()

MpassEta1 = TH1D("MpassEta1",           "top mass in 0<Eta<0.8",             400,  105,  210 )
MpassEta1.Sumw2()

MfailEta2 = TH1D("MfailEta2",           "top mass in 0.8<Eta<2.4",             400,  105,  210 )
MfailEta2.Sumw2()

MpassEta2 = TH1D("MpassEta2",           "top mass in 0.8<Eta<2.4",             400,  105,  210 )
MpassEta2.Sumw2()

ptFullEtaPass = TH1D("ptPass",           "t pt in 0<Eta<2.4 for pass",             400,  0,  2000 )
ptFullEtaFail = TH1D("ptFail",           "t pt in 0<Eta<2.4 for fail",             400,  0,  2000 )

ptFullEtaPass.Sumw2()
ptFullEtaFail.Sumw2()

pteta1pretag.Sumw2()
pteta2pretag.Sumw2()


pteta1.Sumw2()
pteta2.Sumw2()


MtwtptcomparepreSB1e1    = TH2F("MtwtptcomparepreSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwtptcomparepostSB1e1    = TH2F("MtwtptcomparepostSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwtptcomparepreSB1e1.Sumw2()
MtwtptcomparepostSB1e1.Sumw2()

MtwtptcomparepreSB1e2    = TH2F("MtwtptcomparepreSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwtptcomparepostSB1e2    = TH2F("MtwtptcomparepostSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwtptcomparepreSB1e2.Sumw2()
MtwtptcomparepostSB1e2.Sumw2()

Mtwfaileta1          = TH1D("Mtwfaileta1",           "top + W mass fail 0<Eta<0.8",             400,  500,  4000 )
Mtwfaileta1.Sumw2()

Mtwpasseta1          = TH1D("Mtwpasseta1",           "top + w mass pass 0<Eta<0.8",             400,  500,  4000 )
Mtwpasseta1.Sumw2()

MtvsptPasseta1 = TH2F("MtvsptPasseta1",  "Comparison Mt and top pt Pass 0<Eta<0.8",   		400,0,2000, 400,  105,  210 )
MtvsptPasseta1.Sumw2()

MtvsptFaileta1 = TH2F("MtvsptFaileta1",  "Comparison Mt and top pt Fail 0<Eta<0.8",   		400,0,2000, 400,  105,  210 )
MtvsptFaileta1.Sumw2()

Mtwfaileta2          = TH1D("Mtwfaileta2",           "top + W mass fail 0.8<Eta<2.4",             400,  500,  4000 )
Mtwfaileta2.Sumw2()

Mtwpasseta2          = TH1D("Mtwpasseta2",           "top + w mass pass 0.8<Eta<2.4",             400,  500,  4000 )
Mtwpasseta2.Sumw2()

MtvsptPasseta2 = TH2F("MtvsptPasseta2",  "Comparison Mt and top pt Pass 0.8<Eta<2.4",   		400,0,2000, 400,  105,  210 )
MtvsptPasseta2.Sumw2()

MtvsptFaileta2 = TH2F("MtvsptFaileta2",  "Comparison Mt and top pt Fail 0.8<Eta<2.4",   		400,0,2000, 400,  105,  210 )
MtvsptFaileta2.Sumw2()


nev = TH1F("nev",	"nev",		1, 0, 1 )


#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#
eta1Count = 0
eta2Count = 0

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {	"wpt":array('d',[0.]),
				"wmass":array('d',[0.]),
				"tpt":array('d',[0.]),
				"tmass":array('d',[0.]),
				"tau32":array('d',[0.]),
				"tau21":array('d',[0.]),
				"sjbtag":array('d',[0.]),
				"weight":array('d',[0.])}#,"nsubjets":array('d',[0.])


NewTree = Make_Trees(tree_vars)
treeEntries = tree.GetEntries()
nev.SetBinContent(1,B2Gnev)

# Design the splitting if necessary
if jobs != 1:
	evInJob = int(treeEntries/jobs)
	
	lowBinEdge = evInJob*(num-1)
	highBinEdge = evInJob*num

	if num == jobs:
		highBinEdge = treeEntries

else:
	lowBinEdge = 0
	highBinEdge = treeEntries

print "Range of events: (" + str(lowBinEdge) + ", " + str(highBinEdge) + ")"

# syntax to get a var(branch value) from the event is:tree.branchname
for entry in range(lowBinEdge,highBinEdge):
	# Have to grab tree entry first
	tree.GetEntry(entry)

	count	= 	count + 1

	if count % 100000 == 0 :
	  print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/(highBinEdge-lowBinEdge)) + '% -- '

	doneAlready = False

	for hemis in ['hemis0','hemis1']:
		if hemis == 'hemis0':
			# Load up the ttree values
			tVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.topSDmass_leading
			}

			wVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.wSDmass_subleading
			}

		if hemis == 'hemis1' and doneAlready == False  :
			wVals = {
				"tau1":tree.tau1_leading,
				"tau2":tree.tau2_leading,
				"tau3":tree.tau3_leading,
				"phi":tree.phi_leading,
				"mass":tree.mass_leading,
				"pt":tree.pt_leading,
				"eta":tree.eta_leading,
				"sjbtag":tree.sjbtag_leading,
				"SDmass":tree.wSDmass_leading
			}

			tVals = {
				"tau1":tree.tau1_subleading,
				"tau2":tree.tau2_subleading,
				"tau3":tree.tau3_subleading,
				"phi":tree.phi_subleading,
				"mass":tree.mass_subleading,
				"pt":tree.pt_subleading,
				"eta":tree.eta_subleading,
				"sjbtag":tree.sjbtag_subleading,
				"SDmass":tree.topSDmass_subleading
			}

		elif hemis == 'hemis1' and doneAlready == True:
			continue

		# Remake the lorentz vectors
		tjet = TLorentzVector()
		tjet.SetPtEtaPhiM(tVals["pt"],tVals["eta"],tVals["phi"],tVals["mass"])

		wjet = TLorentzVector()
		wjet.SetPtEtaPhiM(wVals["pt"],wVals["eta"],wVals["phi"],wVals["mass"])


		# Initialize weight
		weight = 1.0

		dy_val = abs(tjet.Rapidity()-wjet.Rapidity())

		wpt_cut = wpt[0]<wjet.Perp()<wpt[1]
		tpt_cut = tpt[0]<tjet.Perp()<tpt[1]
		dy_cut = dy[0]<=dy_val<dy[1]

		#We first perform the top and w candidate pt cuts and the deltaY cut
		if wpt_cut and tpt_cut and dy_cut: 
			if options.pdfweights != "nominal":
				if options.pdfweights == 'up':
					iweight = tree.pdf_weightUp
				elif options.pdfweights == 'down':
					iweight = tree.pdf_weightDown
				weight *= iweight


			weightSFt = 1.0
			# weightSFtdown = 1.0
			# weightSFtup = 1.0       
			if options.set!="data":
				#Pileup reweighting is done here 
				bin1 = tree.pileBin

				if options.pileup != 'off':
					weight *= PilePlot.GetBinContent(bin1)
				
				if options.cuts=="default" and options.set.find("QCD") == -1:
					weightSFt = ttagsf
					# weightSFtup = ttagsf + ttagsf_errUp
					# weightSFtdown = ttagsf - ttagsf_errDown

			tmass_cut = tmass[0]<tVals["SDmass"]<tmass[1]

			#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
			if tmass_cut:
				ht = tjet.Perp() + wjet.Perp()

				#MANUAL HT CUT -- TAKE OUT WHEN TRIGGER CORRECTION FINALIZED
				# if ht<1100.0:
				# 	continue 

				# weighttrigup=1.0
				# weighttrigdown=1.0

				if tname != [] and options.set!='data' :
					#Trigger reweighting done here
					TRW = Trigger_Lookup( ht , TrigPlot )[0]
					# TRWup = Trigger_Lookup( ht , TrigPlot )[1]
					# TRWdown = Trigger_Lookup( ht , TrigPlot )[2]

					# weighttrigup=weight*TRWup
					# weighttrigdown=weight*TRWdown
					weight*=TRW

				if options.ptreweight == "on" and options.set.find('ttbar') != -1:
					#ttbar pt reweighting done here
					PTW = tree.pt_reweight
					weight*=PTW
					# weightSFptup=max(0.0,weight*(2*PTW-1))
					# weightSFptdown=weight

				# weightSFtup=weight*weightSFtup
				# weightSFtdown=weight*weightSFtdown
				weight*=weightSFt

				# weighttrigup*=weightSFt
				# weighttrigdown*=weightSFt

				try:
					tau32val		= 	tVals["tau3"]/tVals["tau2"] 
					tau21val		= 	wVals["tau2"]/wVals["tau1"]
				except:
					continue

				tau21_cut =  tau21[0]<=tau21val<tau21[1]
				tau32_cut =  tau32[0]<=tau32val<tau32[1]

				SJ_csvval = tVals["sjbtag"]

				sjbtag_cut = sjbtag[0]<SJ_csvval<=sjbtag[1]

				if type(wmass[0]) is float:
					wmass_cut = wmass[0]<=wVals["SDmass"]<wmass[1]
				elif type(wmass[0]) is list:
					wmass_cut = wmass[0][0]<=wVals["SDmass"]<wmass[0][1] or wmass[1][0]<=wVals["SDmass"]<wmass[1][1] 
				else:
					print "wmass type error"                        

				FullTop = sjbtag_cut and tau32_cut
				if wmass_cut:
					if tau21_cut:
						eta1_cut = eta1[0]<=abs(tjet.Eta())<eta1[1]
						eta2_cut = eta2[0]<=abs(tjet.Eta())<eta2[1]
						#Extract tags and probes for the average b tagging rate here 
						#We use two eta regions 
						if eta1_cut:
							eta1Count += 1
							if not FullTop:
								MtwtptcomparepreSB1e1.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
								pteta1pretag.Fill(tjet.Perp(),weight)
								Mpre.Fill(tjet.M(),weight)

								MfailEta1.Fill(tjet.M(),weight)
								Mtwfaileta1.Fill((tjet+wjet).M(),weight)
								ptFullEtaFail.Fill(tjet.Perp(),weight)
								MtvsptFaileta1.Fill(tjet.Perp(),tjet.M(),weight)
							if FullTop :
								MpostFull.Fill(tjet.M(),weight)
								MtwtptcomparepostSB1e1.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
								pteta1.Fill( tjet.Perp(),weight)

								MpassEta1.Fill(tjet.M(),weight)
		 						Mtwpasseta1.Fill((tjet+wjet).M(),weight)
								ptFullEtaPass.Fill(tjet.Perp(),weight)
								MtvsptPasseta1.Fill(tjet.Perp(),tjet.M(),weight)

						if eta2_cut:
							eta2Count += 1
							if not FullTop:
								MtwtptcomparepreSB1e2.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
								pteta2pretag.Fill( tjet.Perp(),weight)
								Mpre.Fill(tjet.M(),weight)

								MfailEta2.Fill(tjet.M(),weight)
								Mtwfaileta2.Fill((tjet+wjet).M(),weight)
								ptFullEtaFail.Fill(tjet.Perp(),weight)
								MtvsptFaileta2.Fill(tjet.Perp(),tjet.M(),weight)
							if FullTop :
								MpostFull.Fill(tjet.M(),weight)
								MtwtptcomparepostSB1e2.Fill(tjet.Perp(),(tjet+wjet).M(),weight)
								pteta2.Fill( tjet.Perp(),weight)

								MpassEta2.Fill(tjet.M(),weight) 
								Mtwpasseta2.Fill((tjet+wjet).M(),weight)
								ptFullEtaPass.Fill(tjet.Perp(),weight)
								MtvsptPasseta2.Fill(tjet.Perp(),tjet.M(),weight)
						
						temp_variables = {"wpt":wjet.Perp(),"wmass":wVals["SDmass"],"tpt":tVals["pt"],"tmass":tVals["SDmass"],"tau32":tau32val,"tau21":tau21val,"sjbtag":SJ_csvval,"weight":weight}#"nsubjets":nSubjets[tindexval]}
						for tv in tree_vars.keys():
							tree_vars[tv][0] = temp_variables[tv]
						NewTree.Fill()

						doneAlready = True
hEta1Count.SetBinContent(1,eta1Count)
hEta2Count.SetBinContent(1,eta2Count)

f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)

